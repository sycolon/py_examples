# MessengerApp
from mqtt_client import MQTTClient
import tkinter as tk
from tkinter import messagebox
import time
import json

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.create_login_widget()
        self.create_messages_widget()
        self.create_send_widgets()
    
    def create_login_widget(self):
        tk.Label(self.master, text="Name:").grid(row=0, column=0, sticky="we", padx=5, pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1,sticky="we")
        self.login_btn= tk.Button(self.master, text="Login",command=self.create_mqtt_and_connect)
        self.login_btn.grid(row=0,column=2,sticky="we",padx=5, pady=5)

    def create_messages_widget(self):
        tk.Label(self.master, text="All messages:").grid(row=1, column=0, sticky="we", padx=5)
        self.messages_text = tk.Text(self.master)
        self.messages_text.grid(row=3, column=0,columnspan=3,sticky="we", padx=5)
        

    def create_send_widgets(self):
        tk.Label(self.master, text="Message:").grid(row=5, column=0, sticky="we", padx=5)
        self.msg_entry = tk.Entry(self.master)
        self.msg_entry.grid(row=5, column=1,sticky="we")
        self.msg_entry.bind("<Return>", self._send_message_event) # Wenn Eingabe taste gedrückt, wird diese Funktion ausgeführt
        tk.Button(self.master, text="Send",command=self._send_message).grid(row=5,column=2,sticky="we",padx=5)
    
    def _send_message_event(self, event=None):
        self._send_message()
    
    def _send_message(self):
        self._client.publish_message(self._name, self.msg_entry.get())
        self._clear_fields(self.msg_entry)

    def read_messages(self, msg):
        
        payload = json.loads(msg.payload)
        sender= payload['user']
        self._display_message(sender,payload['msg'], payload['timestamp'])
        self._save_read_json(payload)
        #print(msg)
    
    def create_mqtt_and_connect(self):
        self._name = self.name_entry.get()
        self._client = MQTTClient(client_name=self._name, callback=self.read_messages,broker_address='broker.emqx.io') #
        self._client.connect_and_loop_start()
        self.name_entry.config(state='disabled')
        self.login_btn.config(state='disabled')
        self._read_messaging_data()

    
    def _display_message(self, sender, message,timestamp):
        self.messages_text.config(state='normal')
        #current_time = time.strftime("%H:%M:%S")
        self.messages_text.insert(tk.END, f"[{timestamp}] {sender}: {message}\n")
        self.messages_text.see(tk.END) # Scrollt automatisch zum Ende
        self.messages_text.config(state='disabled')

    def on_closing(self):
        if messagebox.askokcancel("Beenden", "Möchten Sie den Messenger wirklich schließen?"):
            self._send_message()
            self._client.disconnect()
            self.master.destroy()

    def _clear_fields(self,entry):
          entry.delete(0, tk.END)
    
    def _add_json_to_text(self, jsonData):
         for json in jsonData:
              self._display_message(json['user'],json['msg'],json['timestamp'])

    def _read_messaging_data(self ):
        filename = f"{self._name}_messaging_data_.json"
        try:
            with open(filename, "r") as jsonfile:
                    _data = json.load(jsonfile)
                    #print(persons_data)
        except json.JSONDecodeError:
            messagebox.showerror("Error","JSON is empty or Brocken") #messagebox
            _data = []
        except FileNotFoundError:
            messagebox.showerror("Error","File not found") #messagebox
            _data = []
        self._add_json_to_text(_data)

    def _save_read_json(self,data ):
        filename = f"{self._name}_messaging_data_.json"
        try:
            with open(filename, "r") as jsonfile:
                    _data = json.load(jsonfile)
                    #print(persons_data)
        except json.JSONDecodeError:
            messagebox.showerror("Error","JSON is empty or Brocken") #messagebox
            _data = []
        except FileNotFoundError:
            messagebox.showerror("Error","File not found") #messagebox
            _data = []
        _data.append(data)

        try:
            with open(filename,"w") as jsonfile:
                    json.dump(_data, jsonfile, indent=4)
        except IOError as e:
            messagebox.showerror("Error",f"Error could'nt write the file {filename}: {e}") #messagebox



root = tk.Tk()
root.geometry("600x450")
root.title("U27 Messaging App")
app = MainApplication(root)
root.protocol("WM_DELETE_WINDOW", app.on_closing)
root.mainloop()