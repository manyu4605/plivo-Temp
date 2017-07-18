import sys
sys.path.insert(0,'../')
import pytest
from random import randint
import time

@pytest.mark.billing
def test_PlivoBilling(plivoDriver,seed):
    """
    Test Case to test whether Amount charged for a message is
    same as Exepected Charge value
    :param plivoDriver: Driver Object for API interaction
    :param seed[0]:Number to be searched for <user input>
    :param seed[1]:Country_iso <user input>
    """

    print "%-50s"%"\nStep 1: Search for Available Phone Numbers .. ",
    code , data = plivoDriver.searching(seed[1],seed[0])
    assert code == 200 , data
    #Check whether atleast 2 numbers match the search criteria
    assert len(data['objects']) > 1 ,"No Free Numbers Available"
    print "[PASS]"
    print "Found %d Matches"%len(data['objects'])


    print "%-50s"%"Step 2: Buy 2 Randomn numbers .. ",
    #Select random indexes from the returned search results
    number1 = data['objects'][randint(0,len(data['objects']))]['number']
    number2 = data['objects'][randint(0,len(data['objects']))]['number']
    for elem in [number1,number2]:
        code , data = plivoDriver.buying(elem)
        assert code == 201,data
        assert data['numbers'][0]['status'] == "Success"
    print "[PASS]"
    print "Numbers bought : %d ,%d"%(int(number1),int(number2))


    print "%-50s"%"Step 3: Log current credit .. ",
    #Store Current credit to be used for later verification
    code, data = plivoDriver.account_details()
    assert code == 200,data
    before_message_credit = float(data['cash_credits'])
    print "[PASS]"
    print "Current Credit : %f"%before_message_credit


    print "%-50s"%"Step 4: Send Message between bought numbers .. ",
    code , data = plivoDriver.message(number1,number2,"Hello World!!")
    assert code == 202,data
    #Assert whether atleast one message UUID is returned
    assert len(data['message_uuid']) > 0,"Message UUID not found"
    message_uuid = data['message_uuid'][0]
    print "[PASS]"


    print "%-50s"%"Step 5: Get rate charged for the message(Using UUID) .. ",
    code , data = plivoDriver.details(message_uuid)
    assert code == 200,data
    #Varify that no error code is returned
    assert data["error_code"] == None
    charged_rate = float(data["total_rate"])
    print "[PASS]"
    print "Actual Rate Charged : %f"%charged_rate


    print "%-50s"%"Step 6: Validate rate charged and expected rate are same ..",
    code , data = plivoDriver.pricing(seed[1])
    assert code == 200,data
    out_rate = float(data['message']['outbound']['rate'])
    assert charged_rate == out_rate
    print "[PASS]"
    print "Expected Out Rate : %f"%out_rate


    print "%-50s"%"Step 7: Validate rate charged and expected rate are same ..",
    charge_timer = 12
    while True:
        """
        Logic to wait for the credit to change
        Max wait is 50 secs after which assert fails
        """
        code , data = plivoDriver.account_details()
        assert code == 200,data
        after_message_credit = float(data['cash_credits'])
        if after_message_credit == before_message_credit and charge_timer != 0:
            charge_timer -= 1
            time.sleep(5)
        else:
            break

    amount_charged = float(before_message_credit) - float(after_message_credit)
    assert round(amount_charged,4) == round(charged_rate,4)

    print "[PASS]"
    print "Remainging Credit: %f"%after_message_credit
