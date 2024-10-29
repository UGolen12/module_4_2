def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    # видим в консоли "Process finished with exit code 0", функция inner_function не срабатывает, пока не вызовешь функцию test_function

test_function()
#inner_function()
#выдает ошибку, потому что эта функция существует только в пространстве имен функции test_function
