import tornado
import tornado.gen
import tornado.web

from core.DCTest import mh
from core.Raspi_MotorHAT import Raspi_MotorHAT


class MotorHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):

        requ_type = self.get_argument('requ_type')

        if requ_type == 'w_down':
            mymotor1 = mh.getMotor(1)
            mymotor1.setSpeed(150)
            mymotor1.run(Raspi_MotorHAT.FORWARD)

            mymotor2 = mh.getMotor(2)
            mymotor2.setSpeed(150)
            mymotor2.run(Raspi_MotorHAT.FORWARD)

            print('W_DOWN')
            self.finish('W_DOWN')

        elif requ_type == 'w_up':
            mymotor1 = mh.getMotor(1)
            mymotor1.run(Raspi_MotorHAT.RELEASE)

            mymotor2 = mh.getMotor(2)
            mymotor2.run(Raspi_MotorHAT.RELEASE)

            print('W_UP')
            self.finish('W_UP')

        elif requ_type == 'a_down':
            mymotor1 = mh.getMotor(1)
            mymotor1.setSpeed(150)
            mymotor1.run(Raspi_MotorHAT.FORWARD)

            mymotor2 = mh.getMotor(2)
            mymotor2.setSpeed(150)
            mymotor2.run(Raspi_MotorHAT.BACKWARD)

            print('A_DOWN')
            self.finish('A_DOWN')

        elif requ_type == 'a_up':
            mymotor1 = mh.getMotor(1)
            mymotor1.run(Raspi_MotorHAT.RELEASE)

            mymotor2 = mh.getMotor(2)
            mymotor2.run(Raspi_MotorHAT.RELEASE)

            print('A_UP')
            self.finish('A_UP')

        elif requ_type == 's_down':
            mymotor1 = mh.getMotor(1)
            mymotor1.setSpeed(150)
            mymotor1.run(Raspi_MotorHAT.BACKWARD)

            mymotor2 = mh.getMotor(2)
            mymotor2.setSpeed(150)
            mymotor2.run(Raspi_MotorHAT.BACKWARD)

            print('S_DOWN')
            self.finish('S_DOWN')

        elif requ_type == 's_up':
            mymotor1 = mh.getMotor(1)
            mymotor1.run(Raspi_MotorHAT.RELEASE)

            mymotor2 = mh.getMotor(2)
            mymotor2.run(Raspi_MotorHAT.RELEASE)

            print('S_UP')
            self.finish('S_UP')

        elif requ_type == 'd_down':
            mymotor1 = mh.getMotor(1)
            mymotor1.setSpeed(150)
            mymotor1.run(Raspi_MotorHAT.BACKWARD)

            mymotor2 = mh.getMotor(2)
            mymotor2.setSpeed(150)
            mymotor2.run(Raspi_MotorHAT.FORWARD)

            print('D_DOWN')
            self.finish('D_DOWN')

        elif requ_type == 'd_up':
            mymotor1 = mh.getMotor(1)
            mymotor1.run(Raspi_MotorHAT.RELEASE)

            mymotor2 = mh.getMotor(2)
            mymotor2.run(Raspi_MotorHAT.RELEASE)

            print('D_UP')
            self.finish('D_UP')

        elif requ_type == 'button_down':

            print('D_UP')
            self.finish('D_UP')
