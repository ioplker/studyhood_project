namespace Studyhood.client
{
    partial class ActionsListForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.Teacher_Schedule_Btn = new System.Windows.Forms.Button();
            this.Teacher_Notifications_Btn = new System.Windows.Forms.Button();
            this.Teacher_Marks_Btn = new System.Windows.Forms.Button();
            this.Teacher_Lessons_Btn = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.Student_Schedule_Btn = new System.Windows.Forms.Button();
            this.Student_Notifications_Btn = new System.Windows.Forms.Button();
            this.Student_Marks_Btn = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.Dispatcher_Schedule_Btn = new System.Windows.Forms.Button();
            this.Dispatcher_Analysis_Btn = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.ClientMgr_EnrolleeRequests_Btn = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.ProgramMgr_EditPlan_Btn = new System.Windows.Forms.Button();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.Deanery_StudentInfo_Btn = new System.Windows.Forms.Button();
            this.Deanery_Notification_Btn = new System.Windows.Forms.Button();
            this.Close_Btn = new System.Windows.Forms.Button();
            this.groupBox7 = new System.Windows.Forms.GroupBox();
            this.Enrollee_Specialities_Btn = new System.Windows.Forms.Button();
            this.Enrollee_SignIn_Btn = new System.Windows.Forms.Button();
            this.groupBox5.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox6.SuspendLayout();
            this.groupBox7.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.Teacher_Schedule_Btn);
            this.groupBox5.Controls.Add(this.Teacher_Notifications_Btn);
            this.groupBox5.Controls.Add(this.Teacher_Marks_Btn);
            this.groupBox5.Controls.Add(this.Teacher_Lessons_Btn);
            this.groupBox5.Location = new System.Drawing.Point(12, 125);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(169, 135);
            this.groupBox5.TabIndex = 16;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "Преподаватель";
            // 
            // Teacher_Schedule_Btn
            // 
            this.Teacher_Schedule_Btn.Location = new System.Drawing.Point(6, 19);
            this.Teacher_Schedule_Btn.Name = "Teacher_Schedule_Btn";
            this.Teacher_Schedule_Btn.Size = new System.Drawing.Size(157, 23);
            this.Teacher_Schedule_Btn.TabIndex = 13;
            this.Teacher_Schedule_Btn.Text = "Расписание занятий";
            this.Teacher_Schedule_Btn.UseVisualStyleBackColor = true;
            this.Teacher_Schedule_Btn.Click += new System.EventHandler(this.open_view_schedule_form);
            // 
            // Teacher_Notifications_Btn
            // 
            this.Teacher_Notifications_Btn.Location = new System.Drawing.Point(6, 48);
            this.Teacher_Notifications_Btn.Name = "Teacher_Notifications_Btn";
            this.Teacher_Notifications_Btn.Size = new System.Drawing.Size(157, 23);
            this.Teacher_Notifications_Btn.TabIndex = 14;
            this.Teacher_Notifications_Btn.Text = "Объявления";
            this.Teacher_Notifications_Btn.UseVisualStyleBackColor = true;
            this.Teacher_Notifications_Btn.Click += new System.EventHandler(this.open_view_notify_form);
            // 
            // Teacher_Marks_Btn
            // 
            this.Teacher_Marks_Btn.Location = new System.Drawing.Point(6, 106);
            this.Teacher_Marks_Btn.Name = "Teacher_Marks_Btn";
            this.Teacher_Marks_Btn.Size = new System.Drawing.Size(157, 23);
            this.Teacher_Marks_Btn.TabIndex = 15;
            this.Teacher_Marks_Btn.Text = "Поставить оценку";
            this.Teacher_Marks_Btn.UseVisualStyleBackColor = true;
            this.Teacher_Marks_Btn.Click += new System.EventHandler(this.open_add_mark_form);
            // 
            // Teacher_Lessons_Btn
            // 
            this.Teacher_Lessons_Btn.Location = new System.Drawing.Point(6, 77);
            this.Teacher_Lessons_Btn.Name = "Teacher_Lessons_Btn";
            this.Teacher_Lessons_Btn.Size = new System.Drawing.Size(157, 23);
            this.Teacher_Lessons_Btn.TabIndex = 13;
            this.Teacher_Lessons_Btn.Text = "Отметить занятие";
            this.Teacher_Lessons_Btn.UseVisualStyleBackColor = true;
            this.Teacher_Lessons_Btn.Click += new System.EventHandler(this.open_mark_lesson_form);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.Student_Schedule_Btn);
            this.groupBox2.Controls.Add(this.Student_Notifications_Btn);
            this.groupBox2.Controls.Add(this.Student_Marks_Btn);
            this.groupBox2.Location = new System.Drawing.Point(12, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(169, 107);
            this.groupBox2.TabIndex = 14;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Студент";
            // 
            // Student_Schedule_Btn
            // 
            this.Student_Schedule_Btn.Location = new System.Drawing.Point(6, 19);
            this.Student_Schedule_Btn.Name = "Student_Schedule_Btn";
            this.Student_Schedule_Btn.Size = new System.Drawing.Size(157, 23);
            this.Student_Schedule_Btn.TabIndex = 10;
            this.Student_Schedule_Btn.Text = "Расписание занятий";
            this.Student_Schedule_Btn.UseVisualStyleBackColor = true;
            this.Student_Schedule_Btn.Click += new System.EventHandler(this.open_view_schedule_form);
            // 
            // Student_Notifications_Btn
            // 
            this.Student_Notifications_Btn.Location = new System.Drawing.Point(6, 48);
            this.Student_Notifications_Btn.Name = "Student_Notifications_Btn";
            this.Student_Notifications_Btn.Size = new System.Drawing.Size(157, 23);
            this.Student_Notifications_Btn.TabIndex = 11;
            this.Student_Notifications_Btn.Text = "Объявления";
            this.Student_Notifications_Btn.UseVisualStyleBackColor = true;
            this.Student_Notifications_Btn.Click += new System.EventHandler(this.open_view_notify_form);
            // 
            // Student_Marks_Btn
            // 
            this.Student_Marks_Btn.Location = new System.Drawing.Point(6, 77);
            this.Student_Marks_Btn.Name = "Student_Marks_Btn";
            this.Student_Marks_Btn.Size = new System.Drawing.Size(157, 23);
            this.Student_Marks_Btn.TabIndex = 12;
            this.Student_Marks_Btn.Text = "Просмотреть оценки";
            this.Student_Marks_Btn.UseVisualStyleBackColor = true;
            this.Student_Marks_Btn.Click += new System.EventHandler(this.open_student_marks_form);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.Dispatcher_Schedule_Btn);
            this.groupBox1.Controls.Add(this.Dispatcher_Analysis_Btn);
            this.groupBox1.Location = new System.Drawing.Point(362, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(169, 79);
            this.groupBox1.TabIndex = 15;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Диспетчер";
            // 
            // Dispatcher_Schedule_Btn
            // 
            this.Dispatcher_Schedule_Btn.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.Dispatcher_Schedule_Btn.Location = new System.Drawing.Point(6, 19);
            this.Dispatcher_Schedule_Btn.Name = "Dispatcher_Schedule_Btn";
            this.Dispatcher_Schedule_Btn.Size = new System.Drawing.Size(157, 23);
            this.Dispatcher_Schedule_Btn.TabIndex = 15;
            this.Dispatcher_Schedule_Btn.Text = "Редактировать расписание";
            this.Dispatcher_Schedule_Btn.UseVisualStyleBackColor = true;
            this.Dispatcher_Schedule_Btn.Click += new System.EventHandler(this.open_edit_schedule_form);
            // 
            // Dispatcher_Analysis_Btn
            // 
            this.Dispatcher_Analysis_Btn.Location = new System.Drawing.Point(6, 48);
            this.Dispatcher_Analysis_Btn.Name = "Dispatcher_Analysis_Btn";
            this.Dispatcher_Analysis_Btn.Size = new System.Drawing.Size(157, 23);
            this.Dispatcher_Analysis_Btn.TabIndex = 16;
            this.Dispatcher_Analysis_Btn.Text = "Анализ нагрузки";
            this.Dispatcher_Analysis_Btn.UseVisualStyleBackColor = true;
            this.Dispatcher_Analysis_Btn.Click += new System.EventHandler(this.open_analysis_form);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.ClientMgr_EnrolleeRequests_Btn);
            this.groupBox3.Location = new System.Drawing.Point(362, 97);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(169, 49);
            this.groupBox3.TabIndex = 20;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Клиент-менеджер";
            // 
            // ClientMgr_EnrolleeRequests_Btn
            // 
            this.ClientMgr_EnrolleeRequests_Btn.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientMgr_EnrolleeRequests_Btn.Location = new System.Drawing.Point(6, 19);
            this.ClientMgr_EnrolleeRequests_Btn.Name = "ClientMgr_EnrolleeRequests_Btn";
            this.ClientMgr_EnrolleeRequests_Btn.Size = new System.Drawing.Size(157, 23);
            this.ClientMgr_EnrolleeRequests_Btn.TabIndex = 15;
            this.ClientMgr_EnrolleeRequests_Btn.Text = "Заявки абитуриентов";
            this.ClientMgr_EnrolleeRequests_Btn.UseVisualStyleBackColor = true;
            this.ClientMgr_EnrolleeRequests_Btn.Click += new System.EventHandler(this.open_add_enrolle_form);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.ProgramMgr_EditPlan_Btn);
            this.groupBox4.Location = new System.Drawing.Point(362, 155);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(169, 49);
            this.groupBox4.TabIndex = 21;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Программный менеджер";
            // 
            // ProgramMgr_EditPlan_Btn
            // 
            this.ProgramMgr_EditPlan_Btn.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ProgramMgr_EditPlan_Btn.Location = new System.Drawing.Point(6, 19);
            this.ProgramMgr_EditPlan_Btn.Name = "ProgramMgr_EditPlan_Btn";
            this.ProgramMgr_EditPlan_Btn.Size = new System.Drawing.Size(157, 23);
            this.ProgramMgr_EditPlan_Btn.TabIndex = 15;
            this.ProgramMgr_EditPlan_Btn.Text = "Редактировать учеб. план";
            this.ProgramMgr_EditPlan_Btn.UseVisualStyleBackColor = true;
            this.ProgramMgr_EditPlan_Btn.Click += new System.EventHandler(this.open_plan_form);
            // 
            // groupBox6
            // 
            this.groupBox6.Controls.Add(this.Deanery_StudentInfo_Btn);
            this.groupBox6.Controls.Add(this.Deanery_Notification_Btn);
            this.groupBox6.Location = new System.Drawing.Point(187, 12);
            this.groupBox6.Name = "groupBox6";
            this.groupBox6.Size = new System.Drawing.Size(169, 79);
            this.groupBox6.TabIndex = 22;
            this.groupBox6.TabStop = false;
            this.groupBox6.Text = "Деканат";
            // 
            // Deanery_StudentInfo_Btn
            // 
            this.Deanery_StudentInfo_Btn.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.Deanery_StudentInfo_Btn.Location = new System.Drawing.Point(6, 19);
            this.Deanery_StudentInfo_Btn.Name = "Deanery_StudentInfo_Btn";
            this.Deanery_StudentInfo_Btn.Size = new System.Drawing.Size(157, 23);
            this.Deanery_StudentInfo_Btn.TabIndex = 15;
            this.Deanery_StudentInfo_Btn.Text = "Информация о студенте";
            this.Deanery_StudentInfo_Btn.UseVisualStyleBackColor = true;
            this.Deanery_StudentInfo_Btn.Click += new System.EventHandler(this.open_student_info_form);
            // 
            // Deanery_Notification_Btn
            // 
            this.Deanery_Notification_Btn.Location = new System.Drawing.Point(6, 48);
            this.Deanery_Notification_Btn.Name = "Deanery_Notification_Btn";
            this.Deanery_Notification_Btn.Size = new System.Drawing.Size(157, 23);
            this.Deanery_Notification_Btn.TabIndex = 16;
            this.Deanery_Notification_Btn.Text = "Сделать объявление";
            this.Deanery_Notification_Btn.UseVisualStyleBackColor = true;
            this.Deanery_Notification_Btn.Click += new System.EventHandler(this.open_add_notify_form);
            // 
            // Close_Btn
            // 
            this.Close_Btn.Location = new System.Drawing.Point(456, 237);
            this.Close_Btn.Name = "Close_Btn";
            this.Close_Btn.Size = new System.Drawing.Size(75, 23);
            this.Close_Btn.TabIndex = 23;
            this.Close_Btn.Text = "Закрыть";
            this.Close_Btn.UseVisualStyleBackColor = true;
            this.Close_Btn.Click += new System.EventHandler(this.close_actions_list_form);
            // 
            // groupBox7
            // 
            this.groupBox7.Controls.Add(this.Enrollee_Specialities_Btn);
            this.groupBox7.Controls.Add(this.Enrollee_SignIn_Btn);
            this.groupBox7.Location = new System.Drawing.Point(187, 97);
            this.groupBox7.Name = "groupBox7";
            this.groupBox7.Size = new System.Drawing.Size(169, 79);
            this.groupBox7.TabIndex = 24;
            this.groupBox7.TabStop = false;
            this.groupBox7.Text = "Абитуриент";
            // 
            // Enrollee_Specialities_Btn
            // 
            this.Enrollee_Specialities_Btn.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.Enrollee_Specialities_Btn.Location = new System.Drawing.Point(6, 19);
            this.Enrollee_Specialities_Btn.Name = "Enrollee_Specialities_Btn";
            this.Enrollee_Specialities_Btn.Size = new System.Drawing.Size(157, 23);
            this.Enrollee_Specialities_Btn.TabIndex = 15;
            this.Enrollee_Specialities_Btn.Text = "Просмотреть направления";
            this.Enrollee_Specialities_Btn.UseVisualStyleBackColor = true;
            this.Enrollee_Specialities_Btn.Click += new System.EventHandler(this.open_specialities_list_form);
            // 
            // Enrollee_SignIn_Btn
            // 
            this.Enrollee_SignIn_Btn.Location = new System.Drawing.Point(6, 48);
            this.Enrollee_SignIn_Btn.Name = "Enrollee_SignIn_Btn";
            this.Enrollee_SignIn_Btn.Size = new System.Drawing.Size(157, 23);
            this.Enrollee_SignIn_Btn.TabIndex = 16;
            this.Enrollee_SignIn_Btn.Text = "Записаться в группу";
            this.Enrollee_SignIn_Btn.UseVisualStyleBackColor = true;
            this.Enrollee_SignIn_Btn.Click += new System.EventHandler(this.open_enrollee_sign_in_form);
            // 
            // ActionsListForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(535, 265);
            this.Controls.Add(this.groupBox7);
            this.Controls.Add(this.Close_Btn);
            this.Controls.Add(this.groupBox6);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox2);
            this.MaximumSize = new System.Drawing.Size(543, 295);
            this.MinimumSize = new System.Drawing.Size(543, 295);
            this.Name = "ActionsListForm";
            this.Text = "ActionsListForm";
            this.groupBox5.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            this.groupBox6.ResumeLayout(false);
            this.groupBox7.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button Teacher_Lessons_Btn;
        private System.Windows.Forms.Button Student_Marks_Btn;
        private System.Windows.Forms.Button Student_Notifications_Btn;
        private System.Windows.Forms.Button Student_Schedule_Btn;
        private System.Windows.Forms.Button Teacher_Schedule_Btn;
        private System.Windows.Forms.Button Teacher_Notifications_Btn;
        private System.Windows.Forms.Button Teacher_Marks_Btn;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button Dispatcher_Schedule_Btn;
        private System.Windows.Forms.Button Dispatcher_Analysis_Btn;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Button ClientMgr_EnrolleeRequests_Btn;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Button ProgramMgr_EditPlan_Btn;
        private System.Windows.Forms.GroupBox groupBox6;
        private System.Windows.Forms.Button Deanery_StudentInfo_Btn;
        private System.Windows.Forms.Button Deanery_Notification_Btn;
        private System.Windows.Forms.Button Close_Btn;
        private System.Windows.Forms.GroupBox groupBox7;
        private System.Windows.Forms.Button Enrollee_Specialities_Btn;
        private System.Windows.Forms.Button Enrollee_SignIn_Btn;

    }
}