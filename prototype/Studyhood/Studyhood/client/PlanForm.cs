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
    public partial class PlanForm : Form
    {
        public PlanForm()
        {
            InitializeComponent();

            this.get_plans();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {  }

        private void get_plans()
        {
            using (var DB = new LiteDatabase(@"StudyhoodData.db"))
            {
                var plan_col = DB.GetCollection<server.Plan>("plan");
                var plan_cont = plan_col.FindAll();

                this.Plan_Table.Rows.Clear();                

                foreach (server.Plan plan in plan_cont)
                {
                    var row = new string[] { plan.Id.ToString(), plan.Speciality_id, plan.Semester, plan.Discipline_id};
                    Plan_Table.Rows.Add(row);
                }

                plan_col.EnsureIndex(x => x.Id);
            }
        }

        private void add_plan(object sender, EventArgs e)
        {
            using (var DB = new LiteDatabase(@"StudyhoodData.db"))
            {
                var plan_col = DB.GetCollection<server.Plan>("plan");
                var new_plan = new server.Plan
                {
                    Speciality_id = Speciality_Combo.Text,
                    Semester = Semester_Combo.Text,
                    Discipline_id = Discipline_Combo.Text,
                };
                plan_col.Insert(new_plan);
                plan_col.EnsureIndex(x => x.Id);

                var row = new string[] { new_plan.Id.ToString(), Speciality_Combo.Text, Semester_Combo.Text, Discipline_Combo.Text};
                Plan_Table.Rows.Add(row);
            }
        }

        private void remove_plan(object sender, EventArgs e)
        {
            using (var DB = new LiteDatabase(@"StudyhoodData.db"))
            {
                var plan_col = DB.GetCollection<server.Plan>("plan");

                var row = Plan_Table.CurrentRow;
                var id = new Guid(row.Cells[0].Value.ToString());
                plan_col.Delete(x => x.Id == id);
                plan_col.EnsureIndex(x => x.Id);

                Plan_Table.Rows.Remove(row);
            }
        }

        private void select_plan(object sender, EventArgs e)
        {
            var row = Plan_Table.CurrentRow;
            if (Plan_Table.Rows.Count > 0)
            {
                Speciality_Combo.Text = row.Cells[1].Value.ToString();
                Semester_Combo.Text = row.Cells[2].Value.ToString();
                Discipline_Combo.Text = row.Cells[3].Value.ToString();
            }
            else
            {
                Speciality_Combo.Text = "";
                Semester_Combo.Text = "";
                Discipline_Combo.Text = "";
            }
        }
    }
}
