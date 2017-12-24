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
    public partial class SpecialityListForm : Form
    {
        public SpecialityListForm()
        {
            InitializeComponent();
        }

        private void open_enrollee_sign_in_form(object sender, EventArgs e)
        {
            client.EnroleeSignInForm EnroleeSignInForm = new client.EnroleeSignInForm();
            EnroleeSignInForm.Owner = this;
            EnroleeSignInForm.Show();
        }
    }
}
