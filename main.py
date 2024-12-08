from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class SimpleApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Título (Label)
        self.label = Label(text="Pressione o botão!", font_size=24, halign="center")
        layout.add_widget(self.label)

        # Botão
        button = Button(text="Clique aqui", size_hint=(1, 0.3), font_size=24)
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        self.label.text = "Olá, Mundo!"


if __name__ == "__main__":
    SimpleApp().run()
