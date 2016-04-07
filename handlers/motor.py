import tornado
import tornado.web
import time
import tornado.gen

# from core.DCTest import mh
# from core.Raspi_MotorHAT import Raspi_MotorHAT
# from handlers import RedisDriver


class MotorHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):

        requ_type = self.get_argument('requ_type')

        if requ_type == 'w_down':
            # myMotor1 = mh.getMotor(1)
            # myMotor1.setSpeed(150)
            # myMotor1.run(Raspi_MotorHAT.FORWARD)

            # myMotor2 = mh.getMotor(2)
            # myMotor2.setSpeed(150)
            # myMotor2.run(Raspi_MotorHAT.FORWARD)

            print('W_DOWN')
            self.finish('W_DOWN')

        elif requ_type == 'w_up':
            # myMotor1 = mh.getMotor(1)
            # myMotor1.run(Raspi_MotorHAT.RELEASE)

            # myMotor2 = mh.getMotor(2)
            # myMotor2.run(Raspi_MotorHAT.RELEASE)

            print('W_UP')
            self.finish('W_UP')

        elif requ_type == 'a_down':
            # myMotor1 = mh.getMotor(1)
            # myMotor1.setSpeed(150)
            # myMotor1.run(Raspi_MotorHAT.FORWARD)

            # myMotor2 = mh.getMotor(2)
            # myMotor2.setSpeed(150)
            # myMotor2.run(Raspi_MotorHAT.BACKWARD)

            print('A_DOWN')
            self.finish('A_DOWN')

        elif requ_type == 'a_up':
            # myMotor1 = mh.getMotor(1)
            # myMotor1.run(Raspi_MotorHAT.RELEASE)

            # myMotor2 = mh.getMotor(2)
            # myMotor2.run(Raspi_MotorHAT.RELEASE)

            print('A_UP')
            self.finish('A_UP')


        elif requ_type == 's_down':
            # myMotor1 = mh.getMotor(1)
            # myMotor1.setSpeed(150)
            # myMotor1.run(Raspi_MotorHAT.BACKWARD)

            # myMotor2 = mh.getMotor(2)
            # myMotor2.setSpeed(150)
            # myMotor2.run(Raspi_MotorHAT.BACKWARD)

            print('S_DOWN')
            self.finish('S_DOWN')

        elif requ_type == 's_up':
            # myMotor1 = mh.getMotor(1)
            # myMotor1.run(Raspi_MotorHAT.RELEASE)

            # myMotor2 = mh.getMotor(2)
            # myMotor2.run(Raspi_MotorHAT.RELEASE)

            print('S_UP')
            self.finish('S_UP')


        elif requ_type == 'd_down':
            # myMotor1 = mh.getMotor(1)
            # myMotor1.setSpeed(150)
            # myMotor1.run(Raspi_MotorHAT.BACKWARD)

            # myMotor2 = mh.getMotor(2)
            # myMotor2.setSpeed(150)
            # myMotor2.run(Raspi_MotorHAT.FORWARD)

            print('D_DOWN')
            self.finish('D_DOWN')

        elif requ_type == 'd_up':
            # myMotor1 = mh.getMotor(1)
            # myMotor1.run(Raspi_MotorHAT.RELEASE)

            # myMotor2 = mh.getMotor(2)
            # myMotor2.run(Raspi_MotorHAT.RELEASE)

            print('D_UP')
            self.finish('D_UP')