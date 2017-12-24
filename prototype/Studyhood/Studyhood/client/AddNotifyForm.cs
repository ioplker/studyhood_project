using LiteDB;
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
    public partial class AddNotifyForm : Form
    {
        public AddNotifyForm()
        {
            InitializeComponent();
        }

        private void add_notify(object sender, EventArgs e)
        {
            using (var DB = new LiteDatabase(@"StudyhoodData.db"))
            {
                var notifications = DB.GetCollection<server.Notify>("notifications");
                var new_notify = new server.Notify { Department = Department_Label.Text, Content = Content_Text.Text};
                notifications.Insert(new_notify);
                notifications.EnsureIndex(x => x.Id);
            }
            
            this.Close();
        }
    }
}
