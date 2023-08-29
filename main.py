from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class BMICalculatorLayout(BoxLayout):
    def calculate_bmi(self):
        try:
            height = float(self.ids.height_input.text) / 100  # Convert cm to meters
            weight = float(self.ids.weight_input.text)
            
            bmi = weight / (height * height)
            
            category = ''
            if bmi < 18.5:
                category = 'Underweight'
            elif 18.5 <= bmi < 24.9:
                category = 'Normal weight'
            elif 25 <= bmi < 29.9:
                category = 'Overweight'
            else:
                category = 'Obese'
            
            self.ids.result_label.text = f'Your BMI: {bmi:.2f}\nCategory: {category}'
        except ValueError:
            self.ids.result_label.text = 'Please enter valid values'

class BMICalculatorApp(App):
    def build(self):
        return BMICalculatorLayout()

if __name__ == '__main__':
    BMICalculatorApp().run()
