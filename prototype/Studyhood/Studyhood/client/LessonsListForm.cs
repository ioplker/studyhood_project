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
    public partial class LessonsListForm : Form
    {
        public LessonsListForm()
        {
            InitializeComponent();
        }

        private void open_present_list_form(object sender, EventArgs e)
        {
            client.PresentListForm PresentListForm = new client.PresentListForm();
            PresentListForm.Owner = this;
            PresentListForm.Show();
        }
    }
}
