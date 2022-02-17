a = int(input("Masukkan angka : "))
b = int(input("Masukkan angka : "))

<<<<<<< HEAD
hasil = a+b
print(hasil)
=======
# program untuk menjalankan calculator
while True:
       
        user_input = input("Tuliskan nilai yang ingin dihitung: ")
        user_input = user_input.strip().split(" ")
                
        user_number1 = int(user_input[0])
        user_number2 = int(user_input[2])
        decision = user_input[1]
                                
        calc = Calculator(user_number1, user_number2)
        result = calc.decision(decision)
        print(result)
                                                
        lanjut = input("Anda ingin melanjutkan perhitungan?: ")
                                                        
        if lanjut.lower()[0] == 'y':
            continue
        else: break
print('Terimakasih')
>>>>>>> run_program
