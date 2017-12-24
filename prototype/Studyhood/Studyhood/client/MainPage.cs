using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Studyhood
{
    public partial class MainPage : Form
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void Login_Btn_Click(object sender, EventArgs e)
        {
            client.LoginForm LoginForm = new client.LoginForm();
            LoginForm.Owner = this;
            LoginForm.Show();
        }

        private void close_main_form(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
