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

        private void Close_Btn_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
