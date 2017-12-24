namespace Studyhood
{
    partial class MainPage
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainPage));
            this.Login_Btn = new System.Windows.Forms.Button();
            this.menu_Panel = new System.Windows.Forms.Panel();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.новостиToolStripMenuItem2 = new System.Windows.Forms.ToolStripMenuItem();
            this.общееToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.контактыToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.выходToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menu_Panel.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // Login_Btn
            // 
            this.Login_Btn.Location = new System.Drawing.Point(564, 12);
            this.Login_Btn.Name = "Login_Btn";
            this.Login_Btn.Size = new System.Drawing.Size(75, 23);
            this.Login_Btn.TabIndex = 6;
            this.Login_Btn.Text = "Войти";
            this.Login_Btn.UseVisualStyleBackColor = true;
            this.Login_Btn.Click += new System.EventHandler(this.Login_Btn_Click);
            // 
            // menu_Panel
            // 
            this.menu_Panel.Controls.Add(this.menuStrip1);
            this.menu_Panel.Location = new System.Drawing.Point(12, 12);
            this.menu_Panel.Name = "menu_Panel";
            this.menu_Panel.Size = new System.Drawing.Size(546, 23);
            this.menu_Panel.TabIndex = 5;
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.новостиToolStripMenuItem2,
            this.общееToolStripMenuItem,
            this.контактыToolStripMenuItem,
            this.выходToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(546, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // новостиToolStripMenuItem2
            // 
            this.новостиToolStripMenuItem2.Name = "новостиToolStripMenuItem2";
            this.новостиToolStripMenuItem2.Size = new System.Drawing.Size(68, 20);
            this.новостиToolStripMenuItem2.Text = "Новости";
            // 
            // общееToolStripMenuItem
            // 
            this.общееToolStripMenuItem.Name = "общееToolStripMenuItem";
            this.общееToolStripMenuItem.Size = new System.Drawing.Size(61, 20);
            this.общееToolStripMenuItem.Text = "О ВУЗе";
            // 
            // контактыToolStripMenuItem
            // 
            this.контактыToolStripMenuItem.Name = "контактыToolStripMenuItem";
            this.контактыToolStripMenuItem.Size = new System.Drawing.Size(75, 20);
            this.контактыToolStripMenuItem.Text = "Контакты";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(12, 41);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(150, 60);
            this.pictureBox1.TabIndex = 9;
            this.pictureBox1.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(168, 41);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.ReadOnly = true;
            this.richTextBox1.Size = new System.Drawing.Size(471, 366);
            this.richTextBox1.TabIndex = 10;
            this.richTextBox1.Text = "<Общая информация>";
            // 
            // richTextBox2
            // 
            this.richTextBox2.Location = new System.Drawing.Point(12, 107);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.ReadOnly = true;
            this.richTextBox2.Size = new System.Drawing.Size(150, 300);
            this.richTextBox2.TabIndex = 11;
            this.richTextBox2.Text = "<Новости>";
            // 
            // выходToolStripMenuItem
            // 
            this.выходToolStripMenuItem.Name = "выходToolStripMenuItem";
            this.выходToolStripMenuItem.Size = new System.Drawing.Size(56, 20);
            this.выходToolStripMenuItem.Text = "Выход";
            this.выходToolStripMenuItem.Click += new System.EventHandler(this.close_main_form);
            // 
            // MainPage
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(651, 419);
            this.Controls.Add(this.richTextBox2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.Login_Btn);
            this.Controls.Add(this.menu_Panel);
            this.Controls.Add(this.pictureBox1);
            this.MaximumSize = new System.Drawing.Size(659, 449);
            this.MinimumSize = new System.Drawing.Size(659, 449);
            this.Name = "MainPage";
            this.Text = "Управление ВУЗом \"Studyhood\"";
            this.menu_Panel.ResumeLayout(false);
            this.menu_Panel.PerformLayout();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button Login_Btn;
        private System.Windows.Forms.Panel menu_Panel;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem общееToolStripMenuItem;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.ToolStripMenuItem новостиToolStripMenuItem2;
        private System.Windows.Forms.ToolStripMenuItem контактыToolStripMenuItem;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.RichTextBox richTextBox2;
        private System.Windows.Forms.ToolStripMenuItem выходToolStripMenuItem;
    }
}