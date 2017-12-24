using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Studyhood.server
{
    class ActualLesson
    {
        public Guid Scheduled_lesson_id { get; set; }
        public Guid Classroom_id { get; set; }
        public Guid Professor_id { get; set; }
        public DateTime Date { get; set; }
    }
}
