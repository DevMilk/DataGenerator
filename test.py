from sample_gen import *

PCount = 50  #Person Count
Login_ = pd.DataFrame(
    data={
        "email": randomEmail(PCount),
        "password": generatePass(PCount),
        "authorization_level": np.random.randint(0, 3, size=PCount)
    })

prinit("Login", Login_)
