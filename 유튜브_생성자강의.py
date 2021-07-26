##.1 def __init__ 함수는 클래스를 선언하는 순간 자동으로 실행되는 함수를 의미한다.

class JSS:

    def __init__(self):

        self.name = input("이름 : ")

        self.age = input("나이 : ")

        print("JSS 클래스 선언!")

    def show(self):

        print("show 실행!")


a = JSS()

# 이와 같이 JSS 클래스를 객체 a에 선언하는 순간 바로 __init__ 함수가 실행되어 __init__ 함수 안의 내용이 자동으로 실행되게 되는 것이다. 일반적으로 클래스에서 반드시 없어선 안될 내용이 클래스 안의 __init__ 함수, 즉, 생성자 안에 정의되게 된다.

class JSS_sample:

    def __init__(self):

        print("JSS_sample 클래스 선언!!")

    def show_sample(self):

        print("show_sample 실행!!")

b = JSS_sample()

# 위의 코드를 실행해보면 볼 수 있는 것처럼 객체 a에 생성자를 포함한 클래스를 선언하기만 해도 생성자안의 내용이 자동으로 실행되게 된다. 클래스 안의 생성자 함수 외의 나머지 함수는 클래스를 객체에 선언한다고해서 자동으로 실행되지는 않는다.

a.show()

b.show_sample()

# 클래스 안에 존재하는 생성자 함수외의 함수를 동작하게 하려면 클래스가 정의된 객체에 직접 접근하여 불러들여야만 실행되게 된다.



class JSS_sample_3:

    def __init__(self):

        self.name = input("이름 : ")

        self.age = input("나이 : ")

        print("JSS 클래스 선언!")

    def show(self):

# 위의 self는 JSS_sample_3 클래스가 저장된 변수 그자체를 의미하고, show 메소드는 JSS_sample_3 클래스에 형성된 name변수와 age변수를 이용하여 표현되므로 show 함수의 인자는 self로 쓰여야 한다.

        print("나의 이름은 {}.나이는 {}세 입니다.".format(self.name,self.age))

# 위의 코드에서 self는 JSS_sample_3 클래스 자신 자체를 의미하는 클래스를 저장할 변수를 의미한다.

# 그러므로, JSS_sample_3 라는 클래스가 선언되자 마자 생성자 함수 def __init__ 안에 동작이 자동으로 실행되게 되고, 그에 따라 self가 이경우 JSS_sample_3 클래스 자체를 의미하므로 JSS_sample_3 클래스에 name이라는 객체가 형성되고 input 함수에 의해 이름을 입력받아 저장되고, age라는 객체가 형성되고 input 함수에 의해 나이를 입력받아 저장되게 된다.

a = JSS_sample_3()

a.show()


# 결국, 위의 코드를 실행하게 되면 a객체에 JSS_sample_3 클래스가 선언되고 자동으로 생성자가 실행되면서 name 변수와 age 변수가 JSS_sample_3 클래스에 형성되게 되고, a 객체에 JSS_sample_3 클래스가 선언되었으므로 show() 함수에 접근 가능하게 되면서, a객체의 show() 함수를 위의 코드처럼 실행할 수 있게 된다.

# 또한, 위의 코드 a.show() 에서 클래스를 정의할 때와 달리 self라는 인자가 포함되지 않은 이유는 이미 a라는 변수에 JSS_sample_3 이라는 클래스가 선언되었으므로 a.show()에서 이미 self의 역할을 하는 a에서 show() 메소드를 불러들인 것 이므로 show() 메소드에 self 인자를 표현할 필요가 없다. 왜냐하면 이미 self가 표현된 것과 마찬가지이기 때문이다.

a.name
a.age

# 또한 a객체에 JSS_sample_3 클래스가 선언되었으므로 JSS_sample_3 클래스에 저장된 변수 name와 age 또한 위와같은 코드로 접근 가능하게 된다.



##.2 클래스의 상속

class JSS_sample_3_new(JSS_sample_3):
# JSS_sample_3_new 클래스는 JSS_sample_3 클래스를 상위클래스로하여 상속받는 다는 것을 의미한다.

    def __init__(self):
    # 상위클래스로 JSS_sample_3를 상속 받았다 하더라도 하위클래스 JSS_sample_3_new에서 이와같이    def __init__ 생성자 함수를 다시 정의하면 상위클래스의 def__init__ 생성자 함수가 같은 이름의 생   성자에 의해 덮어씌어지게 되면서 상위 클래스의 생성자에 저장된 동작들이 하위클래스에서 의미 없어지게     되지만
        super().__init__()
        # 상위클래스의 모든 동작을 상속하여 불러들일 수 있는 super()메소드를 사용하여 상위클래스의          __init__를 불러들이면 하위클래스인 JSS_sample_3_new에서도 def __init__ 생성자를 새롭게       정의하였더라도 상위클래스의 생성자를 사용할 수 있다.

        self.gender = input("성별 : ")
        # 이렇게 상위클래스의 생성자의 모든동작들을 하위클래스에서도 사용할 수 있도록 상속받은 뒤에 하위       클래스 JSS_sample_3_new의 생성자에서 필요한 동작을 새롭게 정의하면 간단하게 상위클래스의 모       든 동작을 하위클래스에서도 사용할 수 있게 한 뒤, 하위클래스에서 새롭게 필요한 동작을 정의하여         하위 클래스를 정의할 수 있다.

    def show(self):

        print("나의 이름은 {}, 성별은 {}자, 나이는 {}세 입니다.".format(self.name, self.gender, self.age))




b = JSS_sample_3_new()

b.JSS_sample_3_new()
b.show()
















