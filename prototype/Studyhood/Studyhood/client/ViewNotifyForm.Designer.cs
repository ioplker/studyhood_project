namespace Studyhood.client
{
    partial class ViewNotifyForm
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.Content_Text = new System.Windows.Forms.RichTextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.Department_Combo = new System.Windows.Forms.ComboBox();
            this.Number_Combo = new System.Windows.Forms.ComboBox();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.Content_Text);
            this.groupBox1.Location = new System.Drawing.Point(15, 68);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(548, 257);
            this.groupBox1.TabIndex = 4;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Объявление";
            // 
            // Content_Text
            // 
            this.Content_Text.Dock = System.Windows.Forms.DockStyle.Fill;
            this.Content_Text.Location = new System.Drawing.Point(3, 16);
            this.Content_Text.Name = "Content_Text";
            this.Content_Text.ReadOnly = true;
            this.Content_Text.Size = new System.Drawing.Size(542, 238);
            this.Content_Text.TabIndex = 0;
            this.Content_Text.Text = "";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(55, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "Кафедра:";
            // 
            // Department_Combo
            // 
            this.Department_Combo.FormattingEnabled = true;
            this.Department_Combo.Items.AddRange(new object[] {
            "АПП",
            "ИУС"});
            this.Department_Combo.Location = new System.Drawing.Point(73, 12);
            this.Department_Combo.Name = "Department_Combo";
            this.Department_Combo.Size = new System.Drawing.Size(98, 21);
            this.Department_Combo.TabIndex = 5;
            this.Department_Combo.Text = "АПП";
            this.Department_Combo.SelectedIndexChanged += new System.EventHandler(this.Department_Combo_SelectedIndexChanged);
            // 
            // Number_Combo
            // 
            this.Number_Combo.FormattingEnabled = true;
            this.Number_Combo.Location = new System.Drawing.Point(15, 39);
            this.Number_Combo.Name = "Number_Combo";
            this.Number_Combo.Size = new System.Drawing.Size(66, 21);
            this.Number_Combo.TabIndex = 8;
            this.Number_Combo.Text = "-";
            this.Number_Combo.SelectedIndexChanged += new System.EventHandler(this.Number_Combo_SelectedIndexChanged);
            // 
            // ViewNotifyForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(575, 337);
            this.Controls.Add(this.Number_Combo);
            this.Controls.Add(this.Department_Combo);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label1);
            this.Name = "ViewNotifyForm";
            this.Text = "ViewNotifyForm";
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RichTextBox Content_Text;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox Department_Combo;
        private System.Windows.Forms.ComboBox Number_Combo;
    }
}