
def  foo():
    aprt_type = int(input('Please enter type on apartment :'))
    
    ratio1 = int(input('Please Enter Ratio of allowted Water (corporator) :'))
    ratio2 = int(input('Please Enter Ratio of allowted Water (borewell) :'))

    
    adding_guest_ = int(input('(enter 0 if no guest) ADD GUEST :')) 

    
    total_point = ratio1 + ratio2
    corporate_ratio = ratio1 / total_point * 100
    
    total_point = ratio1 + ratio2
    borewell_ratio = ratio2 / total_point * 100

    adding_guest = int(input('(enter 0 if no guest) ADD GUEST :')) 
    total_guest = adding_guest + adding_guest_
    water_guest = total_guest * 10 * 30

    
    if aprt_type == 2:
        allowted_water = 900
        borewell_water = borewell_ratio / 100 * allowted_water

        borewell_amount = borewell_water * 1.5

        corporate_water = corporate_ratio / 100 * allowted_water

        corporate_amount = corporate_water * 1

        total_water = borewell_amount + corporate_amount
        tanker_ammount = 0

        if water_guest != 0 :
            if water_guest >= 500:
                _0_to_500 = 500*2
            
            tanker_ammount += 500*2
            val = water_guest - 500 

            if val < 1500:
                tanker_ammount += val*3
            if val > 1500:
                val2 = val-1500
                tanker_ammount += val2*5
            if val > 3000:
                tanker_ammount += val2*8

        print('==========================================')

        print('ALLOT_WATER',  aprt_type, ratio1 ,':', ratio2)
        print('ADD_GUESTS :', total_guest)
        print('BILL : ', allowted_water + water_guest , round(tanker_ammount + total_water))
            
    if aprt_type == 3:
        allowted_water = 1500
        borewell_water = borewell_ratio / 100 * allowted_water

        borewell_amount = borewell_water * 1.5

        corporate_water = corporate_ratio / 100 * allowted_water

        corporate_amount = corporate_water * 1

        total_water = borewell_amount + corporate_amount
        tanker_ammount = 0

        if water_guest != 0 :
            if water_guest >= 500:
                _0_to_500 = 500*2
            
            tanker_ammount += 500*2
            val = water_guest - 500 

            if val < 1500:
                tanker_ammount += val*3
            if val > 1500:
                val2 = val-1500
                tanker_ammount += val2*5
            if val > 3000:
                tanker_ammount += val2*8

        print('==========================================')

        print('ALLOT_WATER',  aprt_type, ratio1 ,':', ratio2)
        print('ADD_GUESTS :', total_guest)
        print('BILL : ', allowted_water + water_guest , round(tanker_ammount + total_water))

foo()






