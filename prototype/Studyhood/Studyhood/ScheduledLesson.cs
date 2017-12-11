using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Studyhood
{
    class ScheduledLesson
    {
        public Guid Id { get; set; }
        public String Type { get; set; }
        public Guid Discipline_id { get; set; }
        public Guid Group_id { get; set; }
        public Guid Classroom_id { get; set; }
        public Guid Professor_id { get; set; }
        public DateTime Date { get; set; }
    }
}
