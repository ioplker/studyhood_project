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
    public partial class LoginForm : Form
    {
        public LoginForm()
        {
            InitializeComponent();
        }

        private void close_login_form(object sender, EventArgs e)
        {
            this.Close();
        }

        private void show_actionslist_form(object sender, EventArgs e)
        {
            client.ActionsListForm ActionsListForm = new client.ActionsListForm();
            ActionsListForm.Owner = this.Owner;
            ActionsListForm.Show();
            this.Close();
        }
    }
}
