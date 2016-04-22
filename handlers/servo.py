import tornado
import tornado.gen
import tornado.web

from core.Raspi_PWM_Servo_Driver import PWM

pwm = PWM(0x6F, debug=True)
pwm.setPWMFreq(60)


class ServoHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):

        requ_type = self.get_argument('requ_type')

        if requ_type == 'up_down':

            pwm.setPWM(0, 200, 100)

            print('UP_DOWN')
            self.finish('UP_DOWN')

        elif requ_type == 'up_up':

            pwm.setPWM(0, 100, 100)

            print('UP_UP')
            self.finish('UP_UP')

        elif requ_type == 'down_down':

            pwm.setPWM(0, 100, 200)

            print('DOWN_DOWN')
            self.finish('DOWN_DOWN')

        elif requ_type == 'down_up':

            pwm.setPWM(0, 100, 100)

            print('DOWN_UP')
            self.finish('DOWN_UP')

        elif requ_type == 'left_down':

            pwm.setPWM(15, 200, 100)

            print('LEFT_DOWN')
            self.finish('LEFT_DOWN')

        elif requ_type == 'left_up':

            pwm.setPWM(15, 100, 100)

            print('LEFT_UP')
            self.finish('Left_UP')

        elif requ_type == 'right_down':

            pwm.setPWM(15, 100, 200)

            print('RIGHT_DOWN')
            self.finish('RIGHT_DOWN')

        elif requ_type == 'right_up':

            pwm.setPWM(15, 100, 100)

            print('RIGHT_UP')
            self.finish('RIGHT_UP')
