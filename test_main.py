
import manage as ma
import student as st
import job as jo


class TestClass:
    def test_maxAcc(self):             #adds accounts so I can test the connection
        filename = "student_data.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()
        stud1 = st.Student("TP1", "P@ssword123", "Tracy", "Pham")
        assert manage.add_student(stud1) == stud1.get_user_name()
        stud2 = st.Student("TP2", "P@ssword123", "Thinh", "Phung")
        assert manage.add_student(stud2) == stud2.get_user_name()
        stud3 = st.Student("DP", "P@ssword123", "Daniel", "Polt")
        assert manage.add_student(stud3) == stud3.get_user_name()
        stud4 = st.Student("KP", "P@ssword123", "Kelvin", "Pun")
        assert manage.add_student(stud4) == stud4.get_user_name()
        stud5 = st.Student("YQ", "P@ssword123", "Yakira", "Quemba")
        assert manage.add_student(stud5) == stud5.get_user_name()

    def test_Connection(self):          
        manage = ma.Manage()
        student = st.Student("TP1", "P@ssword123", "Tracy", "Pham")         #tests cases where there is a match
        assert manage.find_people("Tracy", "Pham") == student.get_user_name()
        stud2 = st.Student("TP2", "P@ssword123", "Thinh", "Phung")
        assert manage.find_people("Thinh", "Phung") == stud2.get_user_name()
        stud3 = st.Student("DP", "P@ssword123", "Daniel", "Polt")
        assert manage.find_people("Daniel", "Polt") == stud3.get_user_name()
        stud4 = st.Student("KP", "P@ssword123", "Kelvin", "Pun")
        assert manage.find_people("Kelvin", "Pun") == stud4.get_user_name()
        stud5 = st.Student("YQ", "P@ssword123", "Yakira", "Quemba")
        assert manage.find_people("Yakira", "Quemba") == stud5.get_user_name()

        assert manage.find_people("Random", "Random") == None           #tests case where theres no match

    def test_Jobs(self):             #adds jobs so I can test the addition
        filename = "job_data.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()
        job1 = jo.Job("Porter", "TransportsItems", "Bridges", "UCA", "10", "TP1")
        assert manage.add_job(job1, "TP1") == job1.get_post_name()
        job2 = jo.Job("Developer", "WritesCode", "USF", "FL", "20", "TP2")
        assert manage.add_job(job2, "TP2") == job2.get_post_name()
        job3 = jo.Job("Tester1", "Tests", "USF", "FL", "20", "DP")
        assert manage.add_job(job3, "DP") == job3.get_post_name()
        job4 = jo.Job("Tester2", "Tests", "USF", "FL", "20", "KP")
        assert manage.add_job(job4, "KP") == job4.get_post_name()
        job5 = jo.Job("SCRUMMaster", "ManagesSCRUM", "USF", "FL", "30", "YQ")
        assert manage.add_job(job5, "YQ") == job5.get_post_name()




