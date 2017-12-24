namespace Studyhood.client
{
    partial class PlanForm
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
            this.Speciality_Combo = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.Semester_Combo = new System.Windows.Forms.ComboBox();
            this.Discipline_Combo = new System.Windows.Forms.ComboBox();
            this.Add_Btn = new System.Windows.Forms.Button();
            this.Remove_Btn = new System.Windows.Forms.Button();
            this.Plan_Table = new System.Windows.Forms.DataGridView();
            this.Id_Column = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Speciality_Col = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Semester_Col = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Discipline_Col = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.Plan_Table)).BeginInit();
            this.SuspendLayout();
            // 
            // Speciality_Combo
            // 
            this.Speciality_Combo.FormattingEnabled = true;
            this.Speciality_Combo.Items.AddRange(new object[] {
            "Информатика и вычислительная техника (09.03.01 – очная, бакалавриат, аккредитован" +
                "о)",
            "Информационные системы и технологии (09.03.02 – очная, бакалавриат, аккредитовано" +
                ")",
            "Программная инженерия (09.03.04 – очная, бакалавриат, аккредитовано)",
            "Информационная безопасность (10.03.01 – очная, бакалавриат, аккредитовано)"});
            this.Speciality_Combo.Location = new System.Drawing.Point(12, 25);
            this.Speciality_Combo.Name = "Speciality_Combo";
            this.Speciality_Combo.Size = new System.Drawing.Size(618, 21);
            this.Speciality_Combo.TabIndex = 0;
            this.Speciality_Combo.Text = "Информатика и вычислительная техника (09.03.01 – очная, бакалавриат, аккредитован" +
                "о)";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(183, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Специальность и форма обучения:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(155, 55);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(73, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "Дисциплина:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(9, 55);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(54, 13);
            this.label3.TabIndex = 3;
            this.label3.Text = "Семестр:";
            // 
            // Semester_Combo
            // 
            this.Semester_Combo.FormattingEnabled = true;
            this.Semester_Combo.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"});
            this.Semester_Combo.Location = new System.Drawing.Point(72, 52);
            this.Semester_Combo.Name = "Semester_Combo";
            this.Semester_Combo.Size = new System.Drawing.Size(58, 21);
            this.Semester_Combo.TabIndex = 4;
            this.Semester_Combo.Text = "1";
            // 
            // Discipline_Combo
            // 
            this.Discipline_Combo.FormattingEnabled = true;
            this.Discipline_Combo.Items.AddRange(new object[] {
            "Русский язык",
            "Вычислительная математика",
            "Сети и телекоммуникации",
            "Экономика",
            "Философия"});
            this.Discipline_Combo.Location = new System.Drawing.Point(234, 52);
            this.Discipline_Combo.Name = "Discipline_Combo";
            this.Discipline_Combo.Size = new System.Drawing.Size(396, 21);
            this.Discipline_Combo.TabIndex = 5;
            this.Discipline_Combo.Text = "Русский язык";
            // 
            // Add_Btn
            // 
            this.Add_Btn.Location = new System.Drawing.Point(12, 79);
            this.Add_Btn.Name = "Add_Btn";
            this.Add_Btn.Size = new System.Drawing.Size(75, 23);
            this.Add_Btn.TabIndex = 6;
            this.Add_Btn.Text = "Добавить";
            this.Add_Btn.UseVisualStyleBackColor = true;
            this.Add_Btn.Click += new System.EventHandler(this.add_plan);
            // 
            // Remove_Btn
            // 
            this.Remove_Btn.Location = new System.Drawing.Point(93, 79);
            this.Remove_Btn.Name = "Remove_Btn";
            this.Remove_Btn.Size = new System.Drawing.Size(75, 23);
            this.Remove_Btn.TabIndex = 7;
            this.Remove_Btn.Text = "Убрать";
            this.Remove_Btn.UseVisualStyleBackColor = true;
            this.Remove_Btn.Click += new System.EventHandler(this.remove_plan);
            // 
            // Plan_Table
            // 
            this.Plan_Table.AllowUserToAddRows = false;
            this.Plan_Table.AllowUserToDeleteRows = false;
            this.Plan_Table.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.Plan_Table.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.Id_Column,
            this.Speciality_Col,
            this.Semester_Col,
            this.Discipline_Col});
            this.Plan_Table.Location = new System.Drawing.Point(12, 108);
            this.Plan_Table.MultiSelect = false;
            this.Plan_Table.Name = "Plan_Table";
            this.Plan_Table.ReadOnly = true;
            this.Plan_Table.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect;
            this.Plan_Table.Size = new System.Drawing.Size(618, 288);
            this.Plan_Table.TabIndex = 8;
            this.Plan_Table.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView1_CellContentClick);
            this.Plan_Table.SelectionChanged += new System.EventHandler(this.select_plan);
            // 
            // Id_Column
            // 
            this.Id_Column.HeaderText = "ID";
            this.Id_Column.Name = "Id_Column";
            this.Id_Column.ReadOnly = true;
            // 
            // Speciality_Col
            // 
            this.Speciality_Col.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.Fill;
            this.Speciality_Col.HeaderText = "Специальность";
            this.Speciality_Col.Name = "Speciality_Col";
            this.Speciality_Col.ReadOnly = true;
            // 
            // Semester_Col
            // 
            this.Semester_Col.HeaderText = "Семестр";
            this.Semester_Col.MaxInputLength = 2;
            this.Semester_Col.Name = "Semester_Col";
            this.Semester_Col.ReadOnly = true;
            this.Semester_Col.Width = 55;
            // 
            // Discipline_Col
            // 
            this.Discipline_Col.HeaderText = "Дисциплина";
            this.Discipline_Col.Name = "Discipline_Col";
            this.Discipline_Col.ReadOnly = true;
            this.Discipline_Col.Width = 200;
            // 
            // PlanForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(642, 408);
            this.Controls.Add(this.Plan_Table);
            this.Controls.Add(this.Remove_Btn);
            this.Controls.Add(this.Add_Btn);
            this.Controls.Add(this.Discipline_Combo);
            this.Controls.Add(this.Semester_Combo);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Speciality_Combo);
            this.Name = "PlanForm";
            this.Text = "PlanForm";
            ((System.ComponentModel.ISupportInitialize)(this.Plan_Table)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox Speciality_Combo;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox Semester_Combo;
        private System.Windows.Forms.ComboBox Discipline_Combo;
        private System.Windows.Forms.Button Add_Btn;
        private System.Windows.Forms.Button Remove_Btn;
        private System.Windows.Forms.DataGridView Plan_Table;
        private System.Windows.Forms.DataGridViewTextBoxColumn Id_Column;
        private System.Windows.Forms.DataGridViewTextBoxColumn Speciality_Col;
        private System.Windows.Forms.DataGridViewTextBoxColumn Semester_Col;
        private System.Windows.Forms.DataGridViewTextBoxColumn Discipline_Col;
    }
}