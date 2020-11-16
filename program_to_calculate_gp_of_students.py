matric_no = input('Enter Your Matric Number ')
password = input('Enter Your surname ')
if '/' in matric_no:
    level = input('Enter Your Current Level ')
    if level == 100:
        faculty = input('Enter Your faculty ')
        upper_fac = faculty.upper()
        department = input('Enter your department ')
        upper_dep = department.upper()
                      if upper_fac == 'TECH' or 'TECHNOlOGY':
                          print('Courses', 'Grades', 'points', 'CGPA')
                                'MTH101' ,
                                'PHY101'
                                'CHM101'
                                'TPD101')
                          if upper_dep == 'CSC':
                              print('CSC101')
                          if upper_dep == 'FST':
                              print('BOT101')
                                
                          
    score_MTH101 = input('Enter your first course score ')
    CHM101 = input('Enter your CHM101 score ')
    PHY101 = input('Enter your PHY101 score ')
    CSC101 = input('Enter your CSC101 score ')
    TPD101 = input('Enter your TPD101 score ')
    score_MTH101_point = input('Enter your MTH101 score ')
    CHM101_point = input('Enter your CHM101 score ')
    PHY101_point = input('Enter your PHY101 score ')
    CSC101_point = input('Enter your CSC101 score ')
    TPD101_point = input('Enter your TPD101 score ')
    each = score_MTH101
    A = [score_MTH101, CHM101, PHY101 , CSC101, TPD101]
    if each in A > 70:
        point == 5
        print('Grade A')
    elif each in A <70:
        point == 4
        print('Grade B')
    elif each in A <60:
        point == 3
        print('Grade C')
    elif each in A <50:
        point == 2
        print('Grade D')
    elif each in A <45:
        point == 1
        print('Grade E')
    elif each in A <40:
        point == 0
        print('Grade F')
    else:
        print('Not A Score!')
else:
    print('Wrong Input!, Try Again')
