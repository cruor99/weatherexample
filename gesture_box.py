from kivy.gesture import GestureDatabase, Gesture
from kivy.uix.boxlayout import BoxLayout

gesture_strings = {
        'left_to_right_line': 'eNq1l01yGzcQhfdzEWljVv83cAF6myodICVLLIllR2KRdGzfPj0N0iZSiQeb4WbIj8BrNB6mAdzvP+///rF52Z3OX4+76ePleYDp/vmA08Pd2+Nfu7vpQPE1HjydHu5O5+P7590pfsp0/+Wg0/1/ijxks+lgs5RH/8P7/u08dytzt/o/3f6YW00HbCOYh/AjuiBN2w+wAQBW94KujFSrFNd5SN/nJjxtYWPuIMTsCi7K8e+nx98Hkgyk08tvY7xc5AmJChcBrFBwQD7TRx+T18pMKODkUqrKsnxJ+TooL4RaDC1aEOGiOqUJ0XAddUp1HlOXglZZAajGvAdblE9jSdeST2Np0Fjp1w3bsn46S3UtfU5vedBbFitQ3SubVyzqy/rpLvNq+mkvD9pLURcEALGSgRZa9pfTX/bV9NNfHvQXSzEHEpEiWN2W50fSX8HV9NNf4dX0018Z9BehGoBciz8vz7+kv+Kr6ae/UtfS1/RXB/0FZS+mxKpcTWPbWNRPf3XQ36ibRjFuKmoUFSjegeUI6bDqihHSYx3y+ENOUlRPIjCmeXO35f1X02Wt60Ww9NlwNEIFrlWJqroZ2fJCsjTaLkbP+kJxDCkIcYgyz1p2VcfYWWIFsVXE2CVhYPhpsumQuqrGCQII4vjDsHyCsPTXfEjcBQnkakBd3iEtvbVbb+N8UKqICheKQ84v9Z+WxiYW9U2X1T19dRxSZ9GialWsxtq3AfU01XlI3RyFPVYOSMzSsqeenvqQp7FAHbBIiboTr2x6Ot8hno673dvPG4HbfCVwn+63AraBaWtQ43E+eJkeZygdrA3CLSwwQ65dywg4w1I6SAndO8gJre8uCRU7qAlZO2gJsQ/kCaHvnhlR6QNlRuR0C2tmRNZ1r5kRSdnU24/ftKDWAudS8evDNy0yV+KawggNSoPWQW2QO2gNYgczVyLvYMuV+u4tV6y3aSG0ZLE1hXKhLVuEnrYM4WKgX2jLCrSnLa3rArrSlhf8K1pLDKgfWcusdxGhpdavwXj9Z4q1WwaI0Gg3tVFBG9WeUqPSU26UeyqNUk+1Uexp5Nbevdfd/uX1PN+Y41q6nRUDfts/n1+TlSnmWxs9v3/ZHR/fnnb5T82TyswvdeHPw/H9+etTasVdMbTEK1TyKFSRbSzq06fNPxQ3LB8=',
        'right_to_left_line': 'eNq1WNtOI0cQfZ8fgZdYXffqH2BfI/EBEQsWoN2ABd4k+/epqR7saQKZfllLyHDcfaZOnerqwpeP3x7/+rm7378ef7zspy/L+6FMl3cHmK4vnm7+3F9MB4xf442m1+uL1+PL87f9a/zJ0+X3g0yXH5Jc57LpoDOVxf7D8+PTcd7m87b6ybbf51XTAVoEcwg/YwvgdFV2BaTEjyiYF1RRmeP5Z/6cpqvfyk6qo1jxolAKgk2vX2/+/zGcj5Hp/vMn3L+Rs7ESY3VQMtjmTuURxBt3cRUkjhjdsSD5mZtr4AImzg4jcXty11/BjZl6hCFuQUQhYjFHE+Ntdkx2GmIHBiqlKjsVMtFt9vQTZYSd3hXLQOzpKJ4dBXDUKhFj1AVxwRW7VvWoHyzkUgkGYk9PsY7UIjGHoHi4MpjaQOyUrhKMsKNTNSBVQqYyQp6mEg2Ri1CtlcwE3dwH2NNUOpuKQFJMUdAwQmRbsYcXhQCQRIuEK9vsaSrZEDsWtkolEoSRmkrb7GkqnU3FODJCGoUHHjHCmTyMjDJycXKzGlW1Sc7pKcMIOQMAYxSpGijrdl44PWUaIY8jVEnchaPgq2xzp6O8arse6iHOiaBiNVwd02IQRkQ6whGvvN2/OA1lGyJ/178G0pKG8qrzxr0QB1BVOJpIsVWpl2JR/14LEDkB0/alIWmpLJY2jqg6VS3MUCXiXPjjo+jskXi1aJEFZSDvkp4K/SL2dFXkzA5qHAcoGoFHnoqdyGHdHqKB1W3ydFXs15CnqVLP5NFHQr5DBUMAqnJml1K5YjT3Gv1xoDlqWqowRK7RGtXdNLpL1NQ2eTqqNEReEQMu1VVB3bYd1XRURxyN1lJVos0oREWVgcjTUB0xFFeNJ05w2e4BmoZqHSGPoahEv418SBGTbUMtDbWVoXFjaBBECmIIgFrOOY+LP24LJdIYXyoOjDCWjhoNsceEhMISKcGY8Hw7MZaO2trREjUSUwyCWzyF8cxuBAZci0N09prk8/x/+7LfP52medN5nDebLq9AZVemq7hg4u14iGZyM4PWgTVBhzXoJcHqDeQGwgxGDXcgJojUgdTAfjsnSP12aeASkjRQE2TsQrIGdorcG6gdmIrChjVYUxFqDzZFRh3YFL0lxHZ1/ZoXNHXOny5oSr22Bf7fBU31W3o/WJAZiMbx6YLMBuF8Y6xe+snqTBPRSVLqrA20NRitOlEuPZqJijGsp+Z5CS1LMm0xZefGjHxGM1cxcTdUFzQTxOUDusLLEmlLWnQnNPPCwD1qDZUeTdGM3D86VTNRh0JpaO3RVM1LHZ5QbOg7Bmpo/zRoQvkdb9MmC8OSY2jaRHu0aZPao02blh5t2hQ6FJs2xR5t2pbzcEKbtqVDnNCmzT4otuLLkibUlke/oU2oSY82oeY92oR66eonZsOb1uUe9o/3D8f86qFOV1EB68rxaBmx5u/Hu+NDfvsQHJT1EOjx+fv+5ebpdp+fQN68M7405D8OL893P26TOv5vusJdXMseM0UojFZb5vb+dfcvS9NvIw==',
       'down_to_top_line': 'eNq1WNtuHDcMfZ8fiV9qiFdRP+C+FsgHFG6ycIyk9sLetM3fl6K0M1Iy7RpddB+88ZkzRyQPJdG5efz8+Me324fD6+nry2H5uX8f03Lz8QjL+3dP978f3i1H9H/6Fy2v79+9nl6ePx9e/Vdebr4cZbnZFXkftOWoVSr7+8fnx6dTfc3qa+UfXvulspYjtAhqCN/8FcDl7qd0K4lzSQwFFDRrhPNXfUzxOEmiAoKsTAnRbHn97f7fl+FYRpaHvgIrWmYU4JJTkrK8PpzFOVPJAqiq/p2SXlaP3CFv6iQFDZgyoGQuNMozJ6qyJRXMQHRZ3kK+rPJUpk8e1EkYweuSFbOR4EVxDAMQNnGxZGSEREJYUAd1TOwVS2yGwlTeEDtiyNMmv9XcLCHzIA+ZxYuPJSkXfUPhMWzFzVY6t4yy5qT+ZFBnViJLhdwDAyuX5cNX3HxFK4ggomaKmEdbk3EWEm+ZWnb/XFYPW3GzFWVuylEd2TKRd7vn5O5muShPYSxtxiKmsS3pWv1wljZnwZgJgHJGFkmqV+qHt7R5C1PjkF0bf5hLm7kQe9UkYSlc/Rz1xTuG2LctevfQG9TDXNrMTSXrcKqxXaPO4S1v3qa15cW0bs7rasPhLW/eprOrViza6Er98JY3b5Pv/aKcMljdBH4M9AXqo/W0FPPDQfNl+bCWu7X1zC0wLCCFN3Xw6DGjmlAxgjccOhzWclnVt7jr5lUcxMUP4kxm5Fl4B1y+qCScFTiLw1rx2LjrTVLF/cRJfkFZ0pTNLlddwlWhVZun0zLzNdrhqMiqLXPgumlv9xP6JZvx8iUi4aesfmLKeThsDK8SDztltRPHUwB8urhGXMNOXe3E2J5KPmMkIStXaYedutqJozCuV99/akMNO3W1k/rB0hfIV3SKhpm6mknjseJb6BrpsFJXK7mXot/YeoV0DiMz/B/S4WNefeRt+CL2a+GaLZ/Dx7z6yOPM6/1wYcvXvwI+vBwOT+tMn7UO9TkvN3dS4DYtdz4G+Rk9fHQ5Hb3F7gcG7zDKyDDXcNBSA7GBuYEwgvHlIDaQGii300TMlUGNwZXhjb/D4MaQxtgJ0qsQDG0M22FoY1gwgFtwuYKaIjfCHrE1MNIgwp14SmNQY8iPq5XUGC1iKjsMGBkMOwycGBLBFWpgS5RLA7mBOUBpFhWZQG2gjqDCj7mVPDF2KllsZGTcYZSRYSmWhpQmVDoKI1p23IeEE0X3KGNZeK9DIPFEKX35sUrc26IOFyN65o6lYcS9OGyi2B6lFycakWkvVOiVKkGpvREoTGivH7TiQHSrj2M7K0IrDkS7+p9WeyvyRLE9SqtUlOiOs/XldURtL2FoZYPoYx/w9ig2UHyI3Fu+jBToNcE0obmjMKJ9W/uEMKHfVSoYY6GEtL/HQ4rCvZtRJvS8hk5obyfME9qdQxtRmZOGYJSJQT8yKE2MvMOAkaE9esIJ7XESjWju1aQp/7PxNOWf+xahKf9+WfjwN6FnhSn/73d+MMb8NfXYOU1od4lh8K5twIp6nu16/HR4fPh0qv815fe0H8n0fRs658/Hj6dPQWG/q6q+g6fnL4eX+6cPh3ggMTNXvN/jvx5fnj9+/dCU1V+7zV6FOhn4pOg/6vV8+zfaneTS'
}

gestures = GestureDatabase()
for name, gesture_string in gesture_strings.items():
    gesture = gestures.str_to_gesture(gesture_string)
    gesture.name = name
    gestures.add_gesture(gesture)
class GestureBox(BoxLayout):

    def __init__(self, **kwargs):
        for name in gesture_strings:
            self.register_event_type('on_{}'.format(name))
        super(GestureBox, self).__init__(**kwargs)


    def on_left_to_right_line(self):
        pass

    def on_right_to_left_line(self):
        pass

    def on_down_to_top_line(self):
        pass

    def on_touch_down(self, touch):
        touch.ud['gesture_path'] = [(touch.x, touch.y)]
        super(GestureBox, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud['gesture_path'].append((touch.x, touch.y))
        super(GestureBox, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if 'gesture_path' in touch.ud:
            gesture = Gesture()
            gesture.add_stroke(touch.ud['gesture_path'])
            gesture.normalize()
            match = gestures.find(gesture, minscore=0.6666660)
            if match:
                print("{} happened".format(match[1].name))
        super(GestureBox, self).on_touch_up(touch)
