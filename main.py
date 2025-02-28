from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class NoteApp(App):
    def build(self):
        self.notes = []  # Danh sách lưu ghi chú

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Ô nhập ghi chú
        self.input_note = TextInput(hint_text="Nhập ghi chú...", size_hint=(1, 0.2))
        layout.add_widget(self.input_note)

        # Nút thêm ghi chú
        add_button = Button(text="Thêm Ghi Chú", size_hint=(1, 0.15))
        add_button.bind(on_press=self.add_note)
        layout.add_widget(add_button)

        # Khu vực hiển thị ghi chú (dùng ScrollView)
        self.notes_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        self.notes_layout.bind(minimum_height=self.notes_layout.setter('height'))

        scroll = ScrollView(size_hint=(1, 0.65))
        scroll.add_widget(self.notes_layout)
        layout.add_widget(scroll)

        return layout

    def add_note(self, instance):
        text = self.input_note.text.strip()
        if text:
            # Tạo một Box chứa ghi chú + nút xóa
            note_box = BoxLayout(size_hint_y=None, height=50)

            note_label = Label(text=text, size_hint_x=0.8)
            delete_button = Button(text="X", size_hint_x=0.2)
            delete_button.bind(on_press=lambda btn: self.delete_note(note_box))

            note_box.add_widget(note_label)
            note_box.add_widget(delete_button)

            self.notes_layout.add_widget(note_box)
            self.notes.append(note_box)

            self.input_note.text = ""  # Xóa nội dung sau khi nhập

    def delete_note(self, note_box):
        self.notes_layout.remove_widget(note_box)
        self.notes.remove(note_box)

if __name__ == "__main__":
    NoteApp().run()
