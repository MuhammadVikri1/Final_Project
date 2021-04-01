import smtplib
from email.message import EmailMessage
Pengirim_Email = "ahmadalbedahani@gmail.com"
Penerima_Email = open("List_Penerima.txt")
Password = input('Apa password Emailmu?:) : ')
PesanBaru = EmailMessage()    #membuat objek pada kelas pesan email
PesanBaru['Subject'] = "Undangan Reuni Kampus 2021" #Definisi Subjek Email
PesanBaru['From'] = Pengirim_Email  #Definisi Pengirim Email
PesanBaru['To'] = Penerima_Email  #Definisi Penerim Email
PesanBaru.set_content('Assalamualaikum ... Apa kabar semua? Mari datang reunian :)') #Definisi Isi badan pesan
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Pengirim_Email, Password) #Masuk ke SMTP server
    smtp.send_message(PesanBaru)      #Kirim Email dengan send_message method dengan passing EmailMessage object


#Sumber : https://ichi.pro/id/cara-mengirim-email-menggunakan-python-dengan-lampiran-file-skrip-215012666985067


# Email_Penerima = open("Email_Penerima.txt "r+")
