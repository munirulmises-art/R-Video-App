from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# তোর পছন্দের থিম অনুযায়ী ব্যাকগ্রাউন্ড কালার হালকা সোনালী/নিউট্রাল রাখতে পারিস
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class RVideoApp(App):
    def build(self):
        # মূল লেআউট (লম্বালম্বি)
        self.root_layout = BoxLayout(orientation='vertical')

        # স্ক্রিনের মাঝখানের মূল কন্টেন্ট দেখানোর জায়গা
        self.content_area = BoxLayout(orientation='vertical', padding=20)
        self.screen_label = Label(
            text='[b]Library Screen[/b]', 
            markup=True, 
            font_size='28sp', 
            color=(0.2, 0.2, 0.2, 1)
        )
        self.content_area.add_widget(self.screen_label)
        
        self.root_layout.add_widget(self.content_area)

        # একদম নিচে তোর আঁকা ডিজাইন অনুযায়ী ৫টি মেনুর বটম নেভিগেশন বার
        nav_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), padding=5, spacing=5)

        # ৫টি বাটন: Library, Edit, For You, Inbox, Me
        btn_library = Button(text='Library', background_color=(0.85, 0.65, 0.13, 1))
        btn_edit = Button(text='Edit', background_color=(0.85, 0.65, 0.13, 1))
        btn_foryou = Button(text='For You', background_color=(0.85, 0.65, 0.13, 1))
        btn_inbox = Button(text='Inbox', background_color=(0.85, 0.65, 0.13, 1))
        btn_me = Button(text='Me', background_color=(0.85, 0.65, 0.13, 1))

        # বাটনে ক্লিক করলে স্ক্রিন পরিবর্তনের ফাংশন যুক্ত করা
        btn_library.bind(on_press=lambda x: self.change_screen("Library"))
        btn_edit.bind(on_press=lambda x: self.change_screen("Edit"))
        btn_foryou.bind(on_press=lambda x: self.change_screen("For You"))
        btn_inbox.bind(on_press=lambda x: self.change_screen("Inbox"))
        btn_me.bind(on_press=lambda x: self.change_screen("Me"))

        # নেভিগেশন বারে বাটনগুলো যোগ করা
        nav_layout.add_widget(btn_library)
        nav_layout.add_widget(btn_edit)
        nav_layout.add_widget(btn_foryou)
        nav_layout.add_widget(btn_inbox)
        nav_layout.add_widget(btn_me)

        self.root_layout.add_widget(nav_layout)

        return self.root_layout

    def change_screen(self, screen_name):
        # কোন মেনুতে ক্লিক করা হলো সে অনুযায়ী লেখার পরিবর্তন
        self.screen_label.text = f'[b]{screen_name} Screen[/b]'

if __name__ == '__main__':
    RVideoApp().run()
