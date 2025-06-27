import threading
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        # Поле для ввода текста
        self.input = TextInput(
            size_hint_y=None,
            height=40,
            multiline=False,
            hint_text='Введите текст'
        )
        self.add_widget(self.input)

        # Кнопка отправки
        self.btn = Button(
            text='Отправить',
            size_hint_y=None,
            height=40
        )
        self.btn.bind(on_press=self.send_request)
        self.add_widget(self.btn)

        # Поле для отображения ответа сервера
        self.response_label = Label(
            text='Ответ сервера появится здесь',
            size_hint_y=None,
            height=200
        )
        self.add_widget(self.response_label)

    def send_request(self, instance):
        # Запускаем запрос в отдельном потоке
        threading.Thread(target=self._send_request_thread).start()

    def _send_request_thread(self):
        url = "https://185.87.192.90:5000/compute"
        data = {'text': self.input.text, "apikey"}
        try:
            response = requests.post(url, json=data, timeout=10)
            response_text = response.text
        except Exception as e:
            response_text = f"Ошибка: {e}. Обратитесь ко мне, если ошибка сохраняется дольше 1 часа."

        # Обновляем UI через главный поток
        Clock.schedule_once(lambda dt: self.update_response(response_text))

    def update_response(self, text):
        self.response_label.text = text

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
