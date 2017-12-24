using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Studyhood.client
{
    public partial class ActionsListForm : Form
    {
        public ActionsListForm()
        {
            InitializeComponent();
        }

        private void close_actions_list_form(object sender, EventArgs e)
        {
            this.Close();
        }

        private void open_plan_form(object sender, EventArgs e)
        {
            client.PlanForm PlanForm = new client.PlanForm();
            PlanForm.Owner = this;
            PlanForm.Show();
        }

        private void open_student_info_form(object sender, EventArgs e)
        {
            client.StudentInfoForm StudentInfoForm = new client.StudentInfoForm();
            StudentInfoForm.Owner = this;
            StudentInfoForm.Show();
        }

        private void open_specialities_list_form(object sender, EventArgs e)
        {
            client.SpecialityListForm SpecialityListForm = new client.SpecialityListForm();
            SpecialityListForm.Owner = this;
            SpecialityListForm.Show();
        }

        private void open_enrollee_sign_in_form(object sender, EventArgs e)
        {
            client.EnroleeSignInForm EnroleeSignInForm = new client.EnroleeSignInForm();
            EnroleeSignInForm.Owner = this;
            EnroleeSignInForm.Show();
        }

        private void open_add_enrolle_form(object sender, EventArgs e)
        {
            client.AddEnrolleForm AddEnrolleForm = new client.AddEnrolleForm();
            AddEnrolleForm.Owner = this;
            AddEnrolleForm.Show();
        }

        private void open_student_marks_form(object sender, EventArgs e)
        {
            client.StudentMarksForm StudentMarksForm = new client.StudentMarksForm();
            StudentMarksForm.Owner = this;
            StudentMarksForm.Show();
        }

        private void open_edit_schedule_form(object sender, EventArgs e)
        {
            client.EditScheduleForm EditScheduleForm = new client.EditScheduleForm();
            EditScheduleForm.Owner = this;
            EditScheduleForm.Show();
        }

        private void open_view_schedule_form(object sender, EventArgs e)
        {
            client.ViewScheduleForm ViewScheduleForm = new client.ViewScheduleForm();
            ViewScheduleForm.Owner = this;
            ViewScheduleForm.Show();
        }

        private void open_add_mark_form(object sender, EventArgs e)
        {
            client.AddMarkForm AddMarkForm = new client.AddMarkForm();
            AddMarkForm.Owner = this;
            AddMarkForm.Show();
        }

        private void open_add_notify_form(object sender, EventArgs e)
        {
            client.AddNotifyForm AddNotifyForm = new client.AddNotifyForm();
            AddNotifyForm.Owner = this;
            AddNotifyForm.Show();
        }

        private void open_view_notify_form(object sender, EventArgs e)
        {
            client.ViewNotifyForm ViewNotifyForm = new client.ViewNotifyForm();
            ViewNotifyForm.Owner = this;
            ViewNotifyForm.Show();
        }

        private void open_mark_lesson_form(object sender, EventArgs e)
        {
            client.LessonsListForm LessonsListForm = new client.LessonsListForm();
            LessonsListForm.Owner = this;
            LessonsListForm.Show();
        }

        private void open_analysis_form(object sender, EventArgs e)
        {
            client.AnalysisForm AnalysisForm = new client.AnalysisForm();
            AnalysisForm.Owner = this;
            AnalysisForm.Show();
        }
    }
}
