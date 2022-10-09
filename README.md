# cn331

# Web Application สำหรับการขอโควตารายวิชา
* Student(User ทั่วไป): สามารถดูรายวิชาที่เปิดให้ขอโควต้า สามารถทำการกดขอโควต้าและกดยกเลิกรายวิชาที่ได้ทำการขอโควต้าได้
* Admin: สามารถจัดการกับรายวิชาต่าง ๆ ได้ผ่าน admin interface สามารถกำหนดข้อมูลต่าง ๆ เกี่ยวกับรายวิชานั้นได้ เช่น เทอมและปีการศึกษาที่เปิด จำนวนที่นั่ง และสามารถกำหนดสถานะว่าจะเปิดหรือปิดรับการขอโควต้าได้

------------
### Log in
![Log in page](https://i.imgur.com/GvB4oK0.png "Login page")

* Local host [http://127.0.0.1:8000](http://127.0.0.1:8000/)

* Heroku link [http://cn331-registrar.herokuapp.com](http://cn331-registrar.herokuapp.com/)

เมื่อกดเข้ามาในหน้าเว็บจะเจอกับหน้า log in เป็นหน้าแรก ผู้ใช้จะต้องทำการ log in ก่อนเข้าใช้

-------------
### User page
![User page](https://i.imgur.com/z7HIHyI.png "User page")

หลังจากทำการ log in เรียบร้อยแล้วจะเจอกับหน้านี้ที่แสดงข้อมูลของผู้ใช้ได้แก่ username และ email โดยผู้ใช้สามารถทำการ log out ได้ด้วยการกดที่ปุ่มบนขวา

---------
### Registrar: Course
![Registrar index](https://i.imgur.com/AqlVKeG.png "Registrar index")

เมื่อกดปุ่ม registrar ที่มุมบนซ้ายจะเจอกับหน้านี้ซึ่งแสดงรายวิชาที่มีการเปิดให้ลงทะเบียน สามารถลงทะเบียนรายวิชาได้ด้วยการคลิกที่ icon ดินสอด้านขวาสุด และสามารถกดดูรายวิชาที่ได้ทำการลงทะเบียนไว้เรียบร้อยแล้วที่ปุม `see your quota`

-----------
### Enrollment result
![Registrar index](https://i.imgur.com/fw91o8O.png "Enrollment")

หากผู้ใช้ทำการกดลงทะเบียนรายวิชา หรือกดที่ปุ่ม `see your quota` ก็จะเจอกับหน้านี้ที่แสดงรายวิชาที่ได้ทำการลงทะเบียนไว้ ผู้ใช้สามารถถอนรายวิชาได้ด้วยการกดที่ปุ่ม `remove`

-----------
### Log out
![Log out](https://i.imgur.com/o5fDMFh.png "Logout page")

เมื่อทำการกดปุ่ม `log out` ผู้ใช้ก็จะกลับมายังหน้า Log in อีกครั้ง

-----------
#### คลิปวีดิโอแสดงการใช้งาน
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=CsbIfaV1rEU)

-----------
## สมาชิกกลุ่ม
- เขมิกา วีรกุลวัฒนา 6310682619
- มุนินทร์ วุฒิพงศ์วรกิจ 6310682601
