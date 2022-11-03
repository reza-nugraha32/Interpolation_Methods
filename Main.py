# Main code ran here

def startup():
    print("Selamat datang!")
    print("1. Metode Interpolasi Newton")
    print("2. Metode Interpolasi Lagrange")
    print("3. Metode Interpolasi Spline")
    print()

    user_input = int(input("Masukkan pilihan Anda : "))
    print()
    
    if user_input == 1:
        print("Pilih orde polinomial Newton")
        print("1. Interpolasi Newton Orde-1")
        print("2. Interpolasi Newton Orde-2")
        print("3. Interpolasi Newton Orde-3")

        user_input = int(input("Masukkan pilihan Anda : "))
        print()
        
        if user_input == 1:
            import Newton_Interpolation_Orde1
        elif user_input == 2:
            import Newton_Interpolation_Orde2
        elif user_input == 3:
            import Newton_Interpolation_Orde3

        restart()
    elif user_input == 2:
        print("Pilih orde polinomial Lagrange")
        print("1. Interpolasi Lagrange Orde-1")
        print("2. Interpolasi Lagrange Orde-2")
        print("3. Interpolasi Lagrange Orde-3")

        user_input = int(input("Masukkan pilihan Anda : "))
        print()
        
        if user_input == 1:
            import Lagrange_Interpolation_Orde1
        elif user_input == 2:
            import Lagrange_Interpolation_Orde2
        elif user_input == 3:
            import Lagrange_Interpolation_Orde3

        restart()

    elif user_input == 3:
        print("Pilih orde polinomial spline")
        print("1. Interpolasi Spline Orde-1")
        print("2. Interpolasi Spline Orde-2")

        user_input = int(input("Masukkan pilihan Anda : "))
        print()
        
        if user_input == 1:
            import Spline_Interpolation_Orde1
        elif user_input == 2:
            import Spline_Interpolation_Orde2

        restart()
    
    else :
        raise TypeError


def restart():
    print()
    user_input = input("Apakah Anda ingin melanjutkan kembali? (y/n) :") 
    if user_input == "y":
        startup()

user_inp = startup()
