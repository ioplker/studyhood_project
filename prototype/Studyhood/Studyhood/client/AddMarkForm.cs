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
    public partial class AddMarkForm : Form
    {
        public AddMarkForm()
        {
            InitializeComponent();
        }

        private void AddMarkForm_Load(object sender, EventArgs e)
        {  }

        private void add_mark(object sender, EventArgs e)
        {
            using (var DB = new LiteDatabase(@"StudyhoodData.db"))
            {
                var marks_col = DB.GetCollection<server.Mark>("marks");
                var new_mark = new server.Mark { Rating_type_id = RatingType_Combo.Text, 
                                                 Date = Date_Picker.Value.ToShortDateString(),
                                                 Name = Mark_Combo.Text,
                                                 Student_id = Student_Combo.Text,
                                                 Discipline_id = Discipline_Combo.Text,
                                                 Work = Work_Edit.Text,
                                                 Teacher_id = Teacher_Lab.Text};
                marks_col.Insert(new_mark);
                marks_col.EnsureIndex(x => x.Id);
            }

            this.Close();
        }
    }
}
