def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius= int(input("Enter a cesius value: "))
    farenheit= celsius*(9/5) +32

    print("The temperature in farenheit is " + str(farenheit))

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
