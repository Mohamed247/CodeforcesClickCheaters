def login(handle, password, driver):
    try:

        handleInputElement = driver.find_element_by_id("handleOrEmail")

    except:
        print("Couldnt find handle element, seems like we are already logged in")
        return

    handleInputElement.send_keys(handle)

    passwordInputElement = driver.find_element_by_id("password")
    passwordInputElement.send_keys(password)

    driver.find_element_by_class_name("submit").click()
