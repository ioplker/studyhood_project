CREATE TABLE Classroom
(
	Classroom_id  integer  NOT NULL ,
	Number  varchar(20)  NULL 
)
go


ALTER TABLE Classroom
	ADD CONSTRAINT  XPKАудитория PRIMARY KEY   NONCLUSTERED (Classroom_id  ASC)
go


CREATE TABLE Discipline
(
	Discipline_id  integer  NOT NULL ,
	Code  varchar(20)  NULL ,
	Name  varchar(20)  NULL 
)
go


ALTER TABLE Discipline
	ADD CONSTRAINT  XPKДисциплина PRIMARY KEY   NONCLUSTERED (Discipline_id  ASC)
go


CREATE TABLE Factual_lesson
(
	Time  datetime  NULL ,
	Classroom_id  integer  NULL ,
	Professor_id  integer  NULL ,
	Scheduled_lesson_id  integer  NOT NULL 
)
go


ALTER TABLE Factual_lesson
	ADD CONSTRAINT  XPKФактическое_занятие PRIMARY KEY   NONCLUSTERED (Scheduled_lesson_id  ASC)
go


CREATE TABLE Group
(
	Group_id  integer  NOT NULL ,
	Code  varchar(20)  NULL ,
	Course  integer  NULL ,
	Speciality_id  integer  NULL 
)
go


ALTER TABLE Group
	ADD CONSTRAINT  XPKГруппа PRIMARY KEY   NONCLUSTERED (Group_id  ASC)
go


CREATE TABLE Mark
(
	Mark_id  integer  NOT NULL ,
	Rating_type_id  integer  NULL ,
	Name  varchar(20)  NULL 
)
go


ALTER TABLE Mark
	ADD CONSTRAINT  XPKОценка PRIMARY KEY   NONCLUSTERED (Mark_id  ASC)
go


CREATE TABLE Plan
(
	Speciality_id  integer  NOT NULL ,
	Discipline_id  integer  NOT NULL 
)
go


ALTER TABLE Plan
	ADD CONSTRAINT  XPKПлан PRIMARY KEY   NONCLUSTERED (Discipline_id  ASC,Speciality_id  ASC)
go


CREATE TABLE Present_students_list
(
	Scheduled_lesson_id  integer  NOT NULL ,
	Student_id  integer  NOT NULL 
)
go


ALTER TABLE Present_students_list
	ADD CONSTRAINT  XPKСписок_присутствующих PRIMARY KEY   NONCLUSTERED (Scheduled_lesson_id  ASC,Student_id  ASC)
go


CREATE TABLE Professor
(
	Professor_id  integer  NOT NULL ,
	FIO  varchar(20)  NULL ,
	Post  varchar(20)  NULL 
)
go


ALTER TABLE Professor
	ADD CONSTRAINT  XPKПреподаватель PRIMARY KEY   NONCLUSTERED (Professor_id  ASC)
go


CREATE TABLE Rating
(
	Discipline_id  integer  NOT NULL ,
	Student_id  integer  NOT NULL ,
	Professor_id  integer  NULL ,
	Rating_type_id  integer  NOT NULL ,
	Mark_id  integer  NULL ,
	Date  datetime  NULL 
)
go


ALTER TABLE Rating
	ADD CONSTRAINT  XPKАттестация PRIMARY KEY   NONCLUSTERED (Discipline_id  ASC,Student_id  ASC,Rating_type_id  ASC)
go


CREATE TABLE Rating_type
(
	Rating_type_id  integer  NOT NULL ,
	Code  varchar(20)  NULL ,
	Name  varchar(20)  NULL 
)
go


ALTER TABLE Rating_type
	ADD CONSTRAINT  XPKВид_аттестации PRIMARY KEY   NONCLUSTERED (Rating_type_id  ASC)
go


CREATE TABLE Scheduled_lesson
(
	Scheduled_lesson_id  integer  NOT NULL ,
	Time  datetime  NULL ,
	Group_id  integer  NULL ,
	Discipline_id  integer  NULL ,
	Classroom_id  integer  NULL ,
	Professor_id  integer  NULL 
)
go


ALTER TABLE Scheduled_lesson
	ADD CONSTRAINT  XPKПлановое_занятие PRIMARY KEY   NONCLUSTERED (Scheduled_lesson_id  ASC)
go


CREATE TABLE Speciality
(
	Speciality_id  integer  NOT NULL ,
	Code  varchar(20)  NULL ,
	Name  varchar(20)  NULL 
)
go


ALTER TABLE Speciality
	ADD CONSTRAINT  XPKНаправление PRIMARY KEY   NONCLUSTERED (Speciality_id  ASC)
go


CREATE TABLE Student
(
	Student_id  integer  NOT NULL ,
	FIO  varchar(20)  NULL ,
	Group_id  integer  NULL 
)
go


ALTER TABLE Student
	ADD CONSTRAINT  XPKСтудент PRIMARY KEY   NONCLUSTERED (Student_id  ASC)
go



ALTER TABLE Factual_lesson
	ADD CONSTRAINT  R_15 FOREIGN KEY (Classroom_id) REFERENCES Classroom(Classroom_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Factual_lesson
	ADD CONSTRAINT  R_16 FOREIGN KEY (Professor_id) REFERENCES Professor(Professor_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Factual_lesson
	ADD CONSTRAINT  R_20 FOREIGN KEY (Scheduled_lesson_id) REFERENCES Scheduled_lesson(Scheduled_lesson_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go



ALTER TABLE Group
	ADD CONSTRAINT  R_2 FOREIGN KEY (Speciality_id) REFERENCES Speciality(Speciality_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go



ALTER TABLE Mark
	ADD CONSTRAINT  R_11 FOREIGN KEY (Rating_type_id) REFERENCES Rating_type(Rating_type_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go



ALTER TABLE Plan
	ADD CONSTRAINT  R_3 FOREIGN KEY (Discipline_id) REFERENCES Discipline(Discipline_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Plan
	ADD CONSTRAINT  R_6 FOREIGN KEY (Speciality_id) REFERENCES Speciality(Speciality_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go



ALTER TABLE Present_students_list
	ADD CONSTRAINT  R_23 FOREIGN KEY (Scheduled_lesson_id) REFERENCES Factual_lesson(Scheduled_lesson_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Present_students_list
	ADD CONSTRAINT  R_24 FOREIGN KEY (Student_id) REFERENCES Student(Student_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go



ALTER TABLE Rating
	ADD CONSTRAINT  R_8 FOREIGN KEY (Student_id) REFERENCES Student(Student_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Rating
	ADD CONSTRAINT  R_9 FOREIGN KEY (Rating_type_id) REFERENCES Rating_type(Rating_type_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Rating
	ADD CONSTRAINT  R_10 FOREIGN KEY (Mark_id) REFERENCES Mark(Mark_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Rating
	ADD CONSTRAINT  R_21 FOREIGN KEY (Discipline_id) REFERENCES Discipline(Discipline_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go



ALTER TABLE Scheduled_lesson
	ADD CONSTRAINT  R_13 FOREIGN KEY (Classroom_id) REFERENCES Classroom(Classroom_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Scheduled_lesson
	ADD CONSTRAINT  R_14 FOREIGN KEY (Professor_id) REFERENCES Professor(Professor_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Scheduled_lesson
	ADD CONSTRAINT  R_18 FOREIGN KEY (Discipline_id) REFERENCES Discipline(Discipline_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go


ALTER TABLE Scheduled_lesson
	ADD CONSTRAINT  R_19 FOREIGN KEY (Group_id) REFERENCES Group(Group_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go



ALTER TABLE Student
	ADD CONSTRAINT  R_7 FOREIGN KEY (Group_id) REFERENCES Group(Group_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go



CREATE TRIGGER tD_Classroom ON Classroom FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Classroom */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Classroom R/13 Scheduled_lesson on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="0002142d", PARENT_OWNER="", PARENT_TABLE="Classroom"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/13", C2P_VERB_PHRASE="R/13", 
    FK_CONSTRAINT="R_13", FK_COLUMNS="Classroom_id" */
    IF EXISTS (
      SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /*  %JoinFKPK(Scheduled_lesson,deleted," = "," AND") */
        Scheduled_lesson.Classroom_id = deleted.Classroom_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Classroom because Scheduled_lesson exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Classroom R/15 Factual_lesson on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Classroom"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/15", C2P_VERB_PHRASE="R/15", 
    FK_CONSTRAINT="R_15", FK_COLUMNS="Classroom_id" */
    IF EXISTS (
      SELECT * FROM deleted,Factual_lesson
      WHERE
        /*  %JoinFKPK(Factual_lesson,deleted," = "," AND") */
        Factual_lesson.Classroom_id = deleted.Classroom_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Classroom because Factual_lesson exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Classroom ON Classroom FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Classroom */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insClassroom_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Classroom R/13 Scheduled_lesson on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00024ca2", PARENT_OWNER="", PARENT_TABLE="Classroom"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/13", C2P_VERB_PHRASE="R/13", 
    FK_CONSTRAINT="R_13", FK_COLUMNS="Classroom_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Classroom_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /*  %JoinFKPK(Scheduled_lesson,deleted," = "," AND") */
        Scheduled_lesson.Classroom_id = deleted.Classroom_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Classroom because Scheduled_lesson exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Classroom R/15 Factual_lesson on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Classroom"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/15", C2P_VERB_PHRASE="R/15", 
    FK_CONSTRAINT="R_15", FK_COLUMNS="Classroom_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Classroom_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Factual_lesson
      WHERE
        /*  %JoinFKPK(Factual_lesson,deleted," = "," AND") */
        Factual_lesson.Classroom_id = deleted.Classroom_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Classroom because Factual_lesson exists.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Discipline ON Discipline FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Discipline */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Discipline R/3 Plan on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00030f73", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Plan"
    P2C_VERB_PHRASE="R/3", C2P_VERB_PHRASE="R/3", 
    FK_CONSTRAINT="R_3", FK_COLUMNS="Discipline_id" */
    IF EXISTS (
      SELECT * FROM deleted,Plan
      WHERE
        /*  %JoinFKPK(Plan,deleted," = "," AND") */
        Plan.Discipline_id = deleted.Discipline_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Discipline because Plan exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Discipline R/18 Scheduled_lesson on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/18", C2P_VERB_PHRASE="R/18", 
    FK_CONSTRAINT="R_18", FK_COLUMNS="Discipline_id" */
    IF EXISTS (
      SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /*  %JoinFKPK(Scheduled_lesson,deleted," = "," AND") */
        Scheduled_lesson.Discipline_id = deleted.Discipline_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Discipline because Scheduled_lesson exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Discipline R/21 Rating on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/21", C2P_VERB_PHRASE="R/21", 
    FK_CONSTRAINT="R_21", FK_COLUMNS="Discipline_id" */
    IF EXISTS (
      SELECT * FROM deleted,Rating
      WHERE
        /*  %JoinFKPK(Rating,deleted," = "," AND") */
        Rating.Discipline_id = deleted.Discipline_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Discipline because Rating exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Discipline ON Discipline FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Discipline */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insDiscipline_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Discipline R/3 Plan on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00035b91", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Plan"
    P2C_VERB_PHRASE="R/3", C2P_VERB_PHRASE="R/3", 
    FK_CONSTRAINT="R_3", FK_COLUMNS="Discipline_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Discipline_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Plan
      WHERE
        /*  %JoinFKPK(Plan,deleted," = "," AND") */
        Plan.Discipline_id = deleted.Discipline_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Discipline because Plan exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Discipline R/18 Scheduled_lesson on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/18", C2P_VERB_PHRASE="R/18", 
    FK_CONSTRAINT="R_18", FK_COLUMNS="Discipline_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Discipline_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /*  %JoinFKPK(Scheduled_lesson,deleted," = "," AND") */
        Scheduled_lesson.Discipline_id = deleted.Discipline_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Discipline because Scheduled_lesson exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Discipline R/21 Rating on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/21", C2P_VERB_PHRASE="R/21", 
    FK_CONSTRAINT="R_21", FK_COLUMNS="Discipline_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Discipline_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Rating
      WHERE
        /*  %JoinFKPK(Rating,deleted," = "," AND") */
        Rating.Discipline_id = deleted.Discipline_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Discipline because Rating exists.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Factual_lesson ON Factual_lesson FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Factual_lesson */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Factual_lesson R/23 Present_students_list on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00056816", PARENT_OWNER="", PARENT_TABLE="Factual_lesson"
    CHILD_OWNER="", CHILD_TABLE="Present_students_list"
    P2C_VERB_PHRASE="R/23", C2P_VERB_PHRASE="R/23", 
    FK_CONSTRAINT="R_23", FK_COLUMNS="Scheduled_lesson_id" */
    IF EXISTS (
      SELECT * FROM deleted,Present_students_list
      WHERE
        /*  %JoinFKPK(Present_students_list,deleted," = "," AND") */
        Present_students_list.Scheduled_lesson_id = deleted.Scheduled_lesson_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Factual_lesson because Present_students_list exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Classroom R/15 Factual_lesson on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Classroom"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/15", C2P_VERB_PHRASE="R/15", 
    FK_CONSTRAINT="R_15", FK_COLUMNS="Classroom_id" */
    IF EXISTS (SELECT * FROM deleted,Classroom
      WHERE
        /* %JoinFKPK(deleted,Classroom," = "," AND") */
        deleted.Classroom_id = Classroom.Classroom_id AND
        NOT EXISTS (
          SELECT * FROM Factual_lesson
          WHERE
            /* %JoinFKPK(Factual_lesson,Classroom," = "," AND") */
            Factual_lesson.Classroom_id = Classroom.Classroom_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Factual_lesson because Classroom exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Professor R/16 Factual_lesson on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Professor"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/16", C2P_VERB_PHRASE="R/16", 
    FK_CONSTRAINT="R_16", FK_COLUMNS="Professor_id" */
    IF EXISTS (SELECT * FROM deleted,Professor
      WHERE
        /* %JoinFKPK(deleted,Professor," = "," AND") */
        deleted.Professor_id = Professor.Professor_id AND
        NOT EXISTS (
          SELECT * FROM Factual_lesson
          WHERE
            /* %JoinFKPK(Factual_lesson,Professor," = "," AND") */
            Factual_lesson.Professor_id = Professor.Professor_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Factual_lesson because Professor exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Scheduled_lesson R/20 Factual_lesson on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Scheduled_lesson"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/20", C2P_VERB_PHRASE="R/20", 
    FK_CONSTRAINT="R_20", FK_COLUMNS="Scheduled_lesson_id" */
    IF EXISTS (SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /* %JoinFKPK(deleted,Scheduled_lesson," = "," AND") */
        deleted.Scheduled_lesson_id = Scheduled_lesson.Scheduled_lesson_id AND
        NOT EXISTS (
          SELECT * FROM Factual_lesson
          WHERE
            /* %JoinFKPK(Factual_lesson,Scheduled_lesson," = "," AND") */
            Factual_lesson.Scheduled_lesson_id = Scheduled_lesson.Scheduled_lesson_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Factual_lesson because Scheduled_lesson exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Factual_lesson ON Factual_lesson FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Factual_lesson */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insScheduled_lesson_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Factual_lesson R/23 Present_students_list on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="0005df6f", PARENT_OWNER="", PARENT_TABLE="Factual_lesson"
    CHILD_OWNER="", CHILD_TABLE="Present_students_list"
    P2C_VERB_PHRASE="R/23", C2P_VERB_PHRASE="R/23", 
    FK_CONSTRAINT="R_23", FK_COLUMNS="Scheduled_lesson_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Scheduled_lesson_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Present_students_list
      WHERE
        /*  %JoinFKPK(Present_students_list,deleted," = "," AND") */
        Present_students_list.Scheduled_lesson_id = deleted.Scheduled_lesson_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Factual_lesson because Present_students_list exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Classroom R/15 Factual_lesson on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Classroom"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/15", C2P_VERB_PHRASE="R/15", 
    FK_CONSTRAINT="R_15", FK_COLUMNS="Classroom_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Classroom_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Classroom
        WHERE
          /* %JoinFKPK(inserted,Classroom) */
          inserted.Classroom_id = Classroom.Classroom_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Classroom_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Factual_lesson because Classroom does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Professor R/16 Factual_lesson on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Professor"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/16", C2P_VERB_PHRASE="R/16", 
    FK_CONSTRAINT="R_16", FK_COLUMNS="Professor_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Professor_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Professor
        WHERE
          /* %JoinFKPK(inserted,Professor) */
          inserted.Professor_id = Professor.Professor_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Professor_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Factual_lesson because Professor does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Scheduled_lesson R/20 Factual_lesson on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Scheduled_lesson"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/20", C2P_VERB_PHRASE="R/20", 
    FK_CONSTRAINT="R_20", FK_COLUMNS="Scheduled_lesson_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Scheduled_lesson_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Scheduled_lesson
        WHERE
          /* %JoinFKPK(inserted,Scheduled_lesson) */
          inserted.Scheduled_lesson_id = Scheduled_lesson.Scheduled_lesson_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Factual_lesson because Scheduled_lesson does not exist.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Group ON Group FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Group */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Group R/7 Student on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00033c83", PARENT_OWNER="", PARENT_TABLE="Group"
    CHILD_OWNER="", CHILD_TABLE="Student"
    P2C_VERB_PHRASE="R/7", C2P_VERB_PHRASE="R/7", 
    FK_CONSTRAINT="R_7", FK_COLUMNS="Group_id" */
    IF EXISTS (
      SELECT * FROM deleted,Student
      WHERE
        /*  %JoinFKPK(Student,deleted," = "," AND") */
        Student.Group_id = deleted.Group_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Group because Student exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Group R/19 Scheduled_lesson on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Group"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/19", C2P_VERB_PHRASE="R/19", 
    FK_CONSTRAINT="R_19", FK_COLUMNS="Group_id" */
    IF EXISTS (
      SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /*  %JoinFKPK(Scheduled_lesson,deleted," = "," AND") */
        Scheduled_lesson.Group_id = deleted.Group_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Group because Scheduled_lesson exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Speciality R/2 Group on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Speciality"
    CHILD_OWNER="", CHILD_TABLE="Group"
    P2C_VERB_PHRASE="R/2", C2P_VERB_PHRASE="R/2", 
    FK_CONSTRAINT="R_2", FK_COLUMNS="Speciality_id" */
    IF EXISTS (SELECT * FROM deleted,Speciality
      WHERE
        /* %JoinFKPK(deleted,Speciality," = "," AND") */
        deleted.Speciality_id = Speciality.Speciality_id AND
        NOT EXISTS (
          SELECT * FROM Group
          WHERE
            /* %JoinFKPK(Group,Speciality," = "," AND") */
            Group.Speciality_id = Speciality.Speciality_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Group because Speciality exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Group ON Group FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Group */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insGroup_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Group R/7 Student on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="0003a242", PARENT_OWNER="", PARENT_TABLE="Group"
    CHILD_OWNER="", CHILD_TABLE="Student"
    P2C_VERB_PHRASE="R/7", C2P_VERB_PHRASE="R/7", 
    FK_CONSTRAINT="R_7", FK_COLUMNS="Group_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Group_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Student
      WHERE
        /*  %JoinFKPK(Student,deleted," = "," AND") */
        Student.Group_id = deleted.Group_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Group because Student exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Group R/19 Scheduled_lesson on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Group"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/19", C2P_VERB_PHRASE="R/19", 
    FK_CONSTRAINT="R_19", FK_COLUMNS="Group_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Group_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /*  %JoinFKPK(Scheduled_lesson,deleted," = "," AND") */
        Scheduled_lesson.Group_id = deleted.Group_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Group because Scheduled_lesson exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Speciality R/2 Group on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Speciality"
    CHILD_OWNER="", CHILD_TABLE="Group"
    P2C_VERB_PHRASE="R/2", C2P_VERB_PHRASE="R/2", 
    FK_CONSTRAINT="R_2", FK_COLUMNS="Speciality_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Speciality_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Speciality
        WHERE
          /* %JoinFKPK(inserted,Speciality) */
          inserted.Speciality_id = Speciality.Speciality_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Speciality_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Group because Speciality does not exist.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Mark ON Mark FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Mark */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Mark R/10 Rating on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00023d8f", PARENT_OWNER="", PARENT_TABLE="Mark"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/10", C2P_VERB_PHRASE="R/10", 
    FK_CONSTRAINT="R_10", FK_COLUMNS="Mark_id" */
    IF EXISTS (
      SELECT * FROM deleted,Rating
      WHERE
        /*  %JoinFKPK(Rating,deleted," = "," AND") */
        Rating.Mark_id = deleted.Mark_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Mark because Rating exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Rating_type R/11 Mark on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Rating_type"
    CHILD_OWNER="", CHILD_TABLE="Mark"
    P2C_VERB_PHRASE="R/11", C2P_VERB_PHRASE="R/11", 
    FK_CONSTRAINT="R_11", FK_COLUMNS="Rating_type_id" */
    IF EXISTS (SELECT * FROM deleted,Rating_type
      WHERE
        /* %JoinFKPK(deleted,Rating_type," = "," AND") */
        deleted.Rating_type_id = Rating_type.Rating_type_id AND
        NOT EXISTS (
          SELECT * FROM Mark
          WHERE
            /* %JoinFKPK(Mark,Rating_type," = "," AND") */
            Mark.Rating_type_id = Rating_type.Rating_type_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Mark because Rating_type exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Mark ON Mark FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Mark */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insMark_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Mark R/10 Rating on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00028a48", PARENT_OWNER="", PARENT_TABLE="Mark"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/10", C2P_VERB_PHRASE="R/10", 
    FK_CONSTRAINT="R_10", FK_COLUMNS="Mark_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Mark_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Rating
      WHERE
        /*  %JoinFKPK(Rating,deleted," = "," AND") */
        Rating.Mark_id = deleted.Mark_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Mark because Rating exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Rating_type R/11 Mark on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Rating_type"
    CHILD_OWNER="", CHILD_TABLE="Mark"
    P2C_VERB_PHRASE="R/11", C2P_VERB_PHRASE="R/11", 
    FK_CONSTRAINT="R_11", FK_COLUMNS="Rating_type_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Rating_type_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Rating_type
        WHERE
          /* %JoinFKPK(inserted,Rating_type) */
          inserted.Rating_type_id = Rating_type.Rating_type_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Rating_type_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Mark because Rating_type does not exist.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Plan ON Plan FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Plan */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Discipline R/3 Plan on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="0002825b", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Plan"
    P2C_VERB_PHRASE="R/3", C2P_VERB_PHRASE="R/3", 
    FK_CONSTRAINT="R_3", FK_COLUMNS="Discipline_id" */
    IF EXISTS (SELECT * FROM deleted,Discipline
      WHERE
        /* %JoinFKPK(deleted,Discipline," = "," AND") */
        deleted.Discipline_id = Discipline.Discipline_id AND
        NOT EXISTS (
          SELECT * FROM Plan
          WHERE
            /* %JoinFKPK(Plan,Discipline," = "," AND") */
            Plan.Discipline_id = Discipline.Discipline_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Plan because Discipline exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Speciality R/6 Plan on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Speciality"
    CHILD_OWNER="", CHILD_TABLE="Plan"
    P2C_VERB_PHRASE="R/6", C2P_VERB_PHRASE="R/6", 
    FK_CONSTRAINT="R_6", FK_COLUMNS="Speciality_id" */
    IF EXISTS (SELECT * FROM deleted,Speciality
      WHERE
        /* %JoinFKPK(deleted,Speciality," = "," AND") */
        deleted.Speciality_id = Speciality.Speciality_id AND
        NOT EXISTS (
          SELECT * FROM Plan
          WHERE
            /* %JoinFKPK(Plan,Speciality," = "," AND") */
            Plan.Speciality_id = Speciality.Speciality_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Plan because Speciality exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Plan ON Plan FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Plan */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insDiscipline_id integer, 
           @insSpeciality_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Discipline R/3 Plan on child update no action */
  /* ERWIN_RELATION:CHECKSUM="0002b667", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Plan"
    P2C_VERB_PHRASE="R/3", C2P_VERB_PHRASE="R/3", 
    FK_CONSTRAINT="R_3", FK_COLUMNS="Discipline_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Discipline_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Discipline
        WHERE
          /* %JoinFKPK(inserted,Discipline) */
          inserted.Discipline_id = Discipline.Discipline_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Plan because Discipline does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Speciality R/6 Plan on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Speciality"
    CHILD_OWNER="", CHILD_TABLE="Plan"
    P2C_VERB_PHRASE="R/6", C2P_VERB_PHRASE="R/6", 
    FK_CONSTRAINT="R_6", FK_COLUMNS="Speciality_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Speciality_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Speciality
        WHERE
          /* %JoinFKPK(inserted,Speciality) */
          inserted.Speciality_id = Speciality.Speciality_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Plan because Speciality does not exist.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Present_students_list ON Present_students_list FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Present_students_list */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Factual_lesson R/23 Present_students_list on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="0002de26", PARENT_OWNER="", PARENT_TABLE="Factual_lesson"
    CHILD_OWNER="", CHILD_TABLE="Present_students_list"
    P2C_VERB_PHRASE="R/23", C2P_VERB_PHRASE="R/23", 
    FK_CONSTRAINT="R_23", FK_COLUMNS="Scheduled_lesson_id" */
    IF EXISTS (SELECT * FROM deleted,Factual_lesson
      WHERE
        /* %JoinFKPK(deleted,Factual_lesson," = "," AND") */
        deleted.Scheduled_lesson_id = Factual_lesson.Scheduled_lesson_id AND
        NOT EXISTS (
          SELECT * FROM Present_students_list
          WHERE
            /* %JoinFKPK(Present_students_list,Factual_lesson," = "," AND") */
            Present_students_list.Scheduled_lesson_id = Factual_lesson.Scheduled_lesson_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Present_students_list because Factual_lesson exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Student R/24 Present_students_list on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Student"
    CHILD_OWNER="", CHILD_TABLE="Present_students_list"
    P2C_VERB_PHRASE="R/24", C2P_VERB_PHRASE="R/24", 
    FK_CONSTRAINT="R_24", FK_COLUMNS="Student_id" */
    IF EXISTS (SELECT * FROM deleted,Student
      WHERE
        /* %JoinFKPK(deleted,Student," = "," AND") */
        deleted.Student_id = Student.Student_id AND
        NOT EXISTS (
          SELECT * FROM Present_students_list
          WHERE
            /* %JoinFKPK(Present_students_list,Student," = "," AND") */
            Present_students_list.Student_id = Student.Student_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Present_students_list because Student exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Present_students_list ON Present_students_list FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Present_students_list */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insScheduled_lesson_id integer, 
           @insStudent_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Factual_lesson R/23 Present_students_list on child update no action */
  /* ERWIN_RELATION:CHECKSUM="0002e2d7", PARENT_OWNER="", PARENT_TABLE="Factual_lesson"
    CHILD_OWNER="", CHILD_TABLE="Present_students_list"
    P2C_VERB_PHRASE="R/23", C2P_VERB_PHRASE="R/23", 
    FK_CONSTRAINT="R_23", FK_COLUMNS="Scheduled_lesson_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Scheduled_lesson_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Factual_lesson
        WHERE
          /* %JoinFKPK(inserted,Factual_lesson) */
          inserted.Scheduled_lesson_id = Factual_lesson.Scheduled_lesson_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Present_students_list because Factual_lesson does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Student R/24 Present_students_list on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Student"
    CHILD_OWNER="", CHILD_TABLE="Present_students_list"
    P2C_VERB_PHRASE="R/24", C2P_VERB_PHRASE="R/24", 
    FK_CONSTRAINT="R_24", FK_COLUMNS="Student_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Student_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Student
        WHERE
          /* %JoinFKPK(inserted,Student) */
          inserted.Student_id = Student.Student_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Present_students_list because Student does not exist.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Professor ON Professor FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Professor */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Professor R/14 Scheduled_lesson on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="0002186c", PARENT_OWNER="", PARENT_TABLE="Professor"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/14", C2P_VERB_PHRASE="R/14", 
    FK_CONSTRAINT="R_14", FK_COLUMNS="Professor_id" */
    IF EXISTS (
      SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /*  %JoinFKPK(Scheduled_lesson,deleted," = "," AND") */
        Scheduled_lesson.Professor_id = deleted.Professor_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Professor because Scheduled_lesson exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Professor R/16 Factual_lesson on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Professor"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/16", C2P_VERB_PHRASE="R/16", 
    FK_CONSTRAINT="R_16", FK_COLUMNS="Professor_id" */
    IF EXISTS (
      SELECT * FROM deleted,Factual_lesson
      WHERE
        /*  %JoinFKPK(Factual_lesson,deleted," = "," AND") */
        Factual_lesson.Professor_id = deleted.Professor_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Professor because Factual_lesson exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Professor ON Professor FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Professor */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insProfessor_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Professor R/14 Scheduled_lesson on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00025938", PARENT_OWNER="", PARENT_TABLE="Professor"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/14", C2P_VERB_PHRASE="R/14", 
    FK_CONSTRAINT="R_14", FK_COLUMNS="Professor_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Professor_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Scheduled_lesson
      WHERE
        /*  %JoinFKPK(Scheduled_lesson,deleted," = "," AND") */
        Scheduled_lesson.Professor_id = deleted.Professor_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Professor because Scheduled_lesson exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Professor R/16 Factual_lesson on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Professor"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/16", C2P_VERB_PHRASE="R/16", 
    FK_CONSTRAINT="R_16", FK_COLUMNS="Professor_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Professor_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Factual_lesson
      WHERE
        /*  %JoinFKPK(Factual_lesson,deleted," = "," AND") */
        Factual_lesson.Professor_id = deleted.Professor_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Professor because Factual_lesson exists.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Rating ON Rating FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Rating */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Student R/8 Rating on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="0004c2fb", PARENT_OWNER="", PARENT_TABLE="Student"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/8", C2P_VERB_PHRASE="R/8", 
    FK_CONSTRAINT="R_8", FK_COLUMNS="Student_id" */
    IF EXISTS (SELECT * FROM deleted,Student
      WHERE
        /* %JoinFKPK(deleted,Student," = "," AND") */
        deleted.Student_id = Student.Student_id AND
        NOT EXISTS (
          SELECT * FROM Rating
          WHERE
            /* %JoinFKPK(Rating,Student," = "," AND") */
            Rating.Student_id = Student.Student_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Rating because Student exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Rating_type R/9 Rating on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Rating_type"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/9", C2P_VERB_PHRASE="R/9", 
    FK_CONSTRAINT="R_9", FK_COLUMNS="Rating_type_id" */
    IF EXISTS (SELECT * FROM deleted,Rating_type
      WHERE
        /* %JoinFKPK(deleted,Rating_type," = "," AND") */
        deleted.Rating_type_id = Rating_type.Rating_type_id AND
        NOT EXISTS (
          SELECT * FROM Rating
          WHERE
            /* %JoinFKPK(Rating,Rating_type," = "," AND") */
            Rating.Rating_type_id = Rating_type.Rating_type_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Rating because Rating_type exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Mark R/10 Rating on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Mark"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/10", C2P_VERB_PHRASE="R/10", 
    FK_CONSTRAINT="R_10", FK_COLUMNS="Mark_id" */
    IF EXISTS (SELECT * FROM deleted,Mark
      WHERE
        /* %JoinFKPK(deleted,Mark," = "," AND") */
        deleted.Mark_id = Mark.Mark_id AND
        NOT EXISTS (
          SELECT * FROM Rating
          WHERE
            /* %JoinFKPK(Rating,Mark," = "," AND") */
            Rating.Mark_id = Mark.Mark_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Rating because Mark exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Discipline R/21 Rating on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/21", C2P_VERB_PHRASE="R/21", 
    FK_CONSTRAINT="R_21", FK_COLUMNS="Discipline_id" */
    IF EXISTS (SELECT * FROM deleted,Discipline
      WHERE
        /* %JoinFKPK(deleted,Discipline," = "," AND") */
        deleted.Discipline_id = Discipline.Discipline_id AND
        NOT EXISTS (
          SELECT * FROM Rating
          WHERE
            /* %JoinFKPK(Rating,Discipline," = "," AND") */
            Rating.Discipline_id = Discipline.Discipline_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Rating because Discipline exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Rating ON Rating FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Rating */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insStudent_id integer, 
           @insDiscipline_id integer, 
           @insRating_type_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Student R/8 Rating on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00056ffe", PARENT_OWNER="", PARENT_TABLE="Student"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/8", C2P_VERB_PHRASE="R/8", 
    FK_CONSTRAINT="R_8", FK_COLUMNS="Student_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Student_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Student
        WHERE
          /* %JoinFKPK(inserted,Student) */
          inserted.Student_id = Student.Student_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Rating because Student does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Rating_type R/9 Rating on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Rating_type"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/9", C2P_VERB_PHRASE="R/9", 
    FK_CONSTRAINT="R_9", FK_COLUMNS="Rating_type_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Rating_type_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Rating_type
        WHERE
          /* %JoinFKPK(inserted,Rating_type) */
          inserted.Rating_type_id = Rating_type.Rating_type_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Rating because Rating_type does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Mark R/10 Rating on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Mark"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/10", C2P_VERB_PHRASE="R/10", 
    FK_CONSTRAINT="R_10", FK_COLUMNS="Mark_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Mark_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Mark
        WHERE
          /* %JoinFKPK(inserted,Mark) */
          inserted.Mark_id = Mark.Mark_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Mark_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Rating because Mark does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Discipline R/21 Rating on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/21", C2P_VERB_PHRASE="R/21", 
    FK_CONSTRAINT="R_21", FK_COLUMNS="Discipline_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Discipline_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Discipline
        WHERE
          /* %JoinFKPK(inserted,Discipline) */
          inserted.Discipline_id = Discipline.Discipline_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Rating because Discipline does not exist.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Rating_type ON Rating_type FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Rating_type */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Rating_type R/9 Rating on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="0001f84e", PARENT_OWNER="", PARENT_TABLE="Rating_type"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/9", C2P_VERB_PHRASE="R/9", 
    FK_CONSTRAINT="R_9", FK_COLUMNS="Rating_type_id" */
    IF EXISTS (
      SELECT * FROM deleted,Rating
      WHERE
        /*  %JoinFKPK(Rating,deleted," = "," AND") */
        Rating.Rating_type_id = deleted.Rating_type_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Rating_type because Rating exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Rating_type R/11 Mark on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Rating_type"
    CHILD_OWNER="", CHILD_TABLE="Mark"
    P2C_VERB_PHRASE="R/11", C2P_VERB_PHRASE="R/11", 
    FK_CONSTRAINT="R_11", FK_COLUMNS="Rating_type_id" */
    IF EXISTS (
      SELECT * FROM deleted,Mark
      WHERE
        /*  %JoinFKPK(Mark,deleted," = "," AND") */
        Mark.Rating_type_id = deleted.Rating_type_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Rating_type because Mark exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Rating_type ON Rating_type FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* UPDATE trigger on Rating_type */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insRating_type_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Rating_type R/9 Rating on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00022783", PARENT_OWNER="", PARENT_TABLE="Rating_type"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/9", C2P_VERB_PHRASE="R/9", 
    FK_CONSTRAINT="R_9", FK_COLUMNS="Rating_type_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Rating_type_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Rating
      WHERE
        /*  %JoinFKPK(Rating,deleted," = "," AND") */
        Rating.Rating_type_id = deleted.Rating_type_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Rating_type because Rating exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Rating_type R/11 Mark on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Rating_type"
    CHILD_OWNER="", CHILD_TABLE="Mark"
    P2C_VERB_PHRASE="R/11", C2P_VERB_PHRASE="R/11", 
    FK_CONSTRAINT="R_11", FK_COLUMNS="Rating_type_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Rating_type_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Mark
      WHERE
        /*  %JoinFKPK(Mark,deleted," = "," AND") */
        Mark.Rating_type_id = deleted.Rating_type_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Rating_type because Mark exists.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Scheduled_lesson ON Scheduled_lesson FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
/* DELETE trigger on Scheduled_lesson */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Scheduled_lesson R/20 Factual_lesson on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="000647ea", PARENT_OWNER="", PARENT_TABLE="Scheduled_lesson"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/20", C2P_VERB_PHRASE="R/20", 
    FK_CONSTRAINT="R_20", FK_COLUMNS="Scheduled_lesson_id" */
    IF EXISTS (
      SELECT * FROM deleted,Factual_lesson
      WHERE
        /*  %JoinFKPK(Factual_lesson,deleted," = "," AND") */
        Factual_lesson.Scheduled_lesson_id = deleted.Scheduled_lesson_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Scheduled_lesson because Factual_lesson exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Classroom R/13 Scheduled_lesson on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Classroom"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/13", C2P_VERB_PHRASE="R/13", 
    FK_CONSTRAINT="R_13", FK_COLUMNS="Classroom_id" */
    IF EXISTS (SELECT * FROM deleted,Classroom
      WHERE
        /* %JoinFKPK(deleted,Classroom," = "," AND") */
        deleted.Classroom_id = Classroom.Classroom_id AND
        NOT EXISTS (
          SELECT * FROM Scheduled_lesson
          WHERE
            /* %JoinFKPK(Scheduled_lesson,Classroom," = "," AND") */
            Scheduled_lesson.Classroom_id = Classroom.Classroom_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Scheduled_lesson because Classroom exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Professor R/14 Scheduled_lesson on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Professor"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/14", C2P_VERB_PHRASE="R/14", 
    FK_CONSTRAINT="R_14", FK_COLUMNS="Professor_id" */
    IF EXISTS (SELECT * FROM deleted,Professor
      WHERE
        /* %JoinFKPK(deleted,Professor," = "," AND") */
        deleted.Professor_id = Professor.Professor_id AND
        NOT EXISTS (
          SELECT * FROM Scheduled_lesson
          WHERE
            /* %JoinFKPK(Scheduled_lesson,Professor," = "," AND") */
            Scheduled_lesson.Professor_id = Professor.Professor_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Scheduled_lesson because Professor exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Discipline R/18 Scheduled_lesson on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/18", C2P_VERB_PHRASE="R/18", 
    FK_CONSTRAINT="R_18", FK_COLUMNS="Discipline_id" */
    IF EXISTS (SELECT * FROM deleted,Discipline
      WHERE
        /* %JoinFKPK(deleted,Discipline," = "," AND") */
        deleted.Discipline_id = Discipline.Discipline_id AND
        NOT EXISTS (
          SELECT * FROM Scheduled_lesson
          WHERE
            /* %JoinFKPK(Scheduled_lesson,Discipline," = "," AND") */
            Scheduled_lesson.Discipline_id = Discipline.Discipline_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Scheduled_lesson because Discipline exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    /* Group R/19 Scheduled_lesson on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Group"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/19", C2P_VERB_PHRASE="R/19", 
    FK_CONSTRAINT="R_19", FK_COLUMNS="Group_id" */
    IF EXISTS (SELECT * FROM deleted,Group
      WHERE
        /* %JoinFKPK(deleted,Group," = "," AND") */
        deleted.Group_id = Group.Group_id AND
        NOT EXISTS (
          SELECT * FROM Scheduled_lesson
          WHERE
            /* %JoinFKPK(Scheduled_lesson,Group," = "," AND") */
            Scheduled_lesson.Group_id = Group.Group_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Scheduled_lesson because Group exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Scheduled_lesson ON Scheduled_lesson FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
/* UPDATE trigger on Scheduled_lesson */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insScheduled_lesson_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:55 */
  /* Scheduled_lesson R/20 Factual_lesson on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00074447", PARENT_OWNER="", PARENT_TABLE="Scheduled_lesson"
    CHILD_OWNER="", CHILD_TABLE="Factual_lesson"
    P2C_VERB_PHRASE="R/20", C2P_VERB_PHRASE="R/20", 
    FK_CONSTRAINT="R_20", FK_COLUMNS="Scheduled_lesson_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Scheduled_lesson_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Factual_lesson
      WHERE
        /*  %JoinFKPK(Factual_lesson,deleted," = "," AND") */
        Factual_lesson.Scheduled_lesson_id = deleted.Scheduled_lesson_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Scheduled_lesson because Factual_lesson exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Classroom R/13 Scheduled_lesson on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Classroom"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/13", C2P_VERB_PHRASE="R/13", 
    FK_CONSTRAINT="R_13", FK_COLUMNS="Classroom_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Classroom_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Classroom
        WHERE
          /* %JoinFKPK(inserted,Classroom) */
          inserted.Classroom_id = Classroom.Classroom_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Classroom_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Scheduled_lesson because Classroom does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Professor R/14 Scheduled_lesson on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Professor"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/14", C2P_VERB_PHRASE="R/14", 
    FK_CONSTRAINT="R_14", FK_COLUMNS="Professor_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Professor_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Professor
        WHERE
          /* %JoinFKPK(inserted,Professor) */
          inserted.Professor_id = Professor.Professor_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Professor_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Scheduled_lesson because Professor does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Discipline R/18 Scheduled_lesson on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Discipline"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/18", C2P_VERB_PHRASE="R/18", 
    FK_CONSTRAINT="R_18", FK_COLUMNS="Discipline_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Discipline_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Discipline
        WHERE
          /* %JoinFKPK(inserted,Discipline) */
          inserted.Discipline_id = Discipline.Discipline_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Discipline_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Scheduled_lesson because Discipline does not exist.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Group R/19 Scheduled_lesson on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Group"
    CHILD_OWNER="", CHILD_TABLE="Scheduled_lesson"
    P2C_VERB_PHRASE="R/19", C2P_VERB_PHRASE="R/19", 
    FK_CONSTRAINT="R_19", FK_COLUMNS="Group_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Group_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Group
        WHERE
          /* %JoinFKPK(inserted,Group) */
          inserted.Group_id = Group.Group_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Group_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Scheduled_lesson because Group does not exist.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Speciality ON Speciality FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
/* DELETE trigger on Speciality */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
    /* Speciality R/2 Group on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="0001ecfa", PARENT_OWNER="", PARENT_TABLE="Speciality"
    CHILD_OWNER="", CHILD_TABLE="Group"
    P2C_VERB_PHRASE="R/2", C2P_VERB_PHRASE="R/2", 
    FK_CONSTRAINT="R_2", FK_COLUMNS="Speciality_id" */
    IF EXISTS (
      SELECT * FROM deleted,Group
      WHERE
        /*  %JoinFKPK(Group,deleted," = "," AND") */
        Group.Speciality_id = deleted.Speciality_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Speciality because Group exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
    /* Speciality R/6 Plan on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Speciality"
    CHILD_OWNER="", CHILD_TABLE="Plan"
    P2C_VERB_PHRASE="R/6", C2P_VERB_PHRASE="R/6", 
    FK_CONSTRAINT="R_6", FK_COLUMNS="Speciality_id" */
    IF EXISTS (
      SELECT * FROM deleted,Plan
      WHERE
        /*  %JoinFKPK(Plan,deleted," = "," AND") */
        Plan.Speciality_id = deleted.Speciality_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Speciality because Plan exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Speciality ON Speciality FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
/* UPDATE trigger on Speciality */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insSpeciality_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Speciality R/2 Group on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00022e72", PARENT_OWNER="", PARENT_TABLE="Speciality"
    CHILD_OWNER="", CHILD_TABLE="Group"
    P2C_VERB_PHRASE="R/2", C2P_VERB_PHRASE="R/2", 
    FK_CONSTRAINT="R_2", FK_COLUMNS="Speciality_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Speciality_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Group
      WHERE
        /*  %JoinFKPK(Group,deleted," = "," AND") */
        Group.Speciality_id = deleted.Speciality_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Speciality because Group exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Speciality R/6 Plan on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Speciality"
    CHILD_OWNER="", CHILD_TABLE="Plan"
    P2C_VERB_PHRASE="R/6", C2P_VERB_PHRASE="R/6", 
    FK_CONSTRAINT="R_6", FK_COLUMNS="Speciality_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Speciality_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Plan
      WHERE
        /*  %JoinFKPK(Plan,deleted," = "," AND") */
        Plan.Speciality_id = deleted.Speciality_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Speciality because Plan exists.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go


CREATE TRIGGER tD_Student ON Student FOR DELETE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
/* DELETE trigger on Student */
BEGIN
  DECLARE  @errno   int,
           @errmsg  varchar(255)
    /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
    /* Student R/8 Rating on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00033652", PARENT_OWNER="", PARENT_TABLE="Student"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/8", C2P_VERB_PHRASE="R/8", 
    FK_CONSTRAINT="R_8", FK_COLUMNS="Student_id" */
    IF EXISTS (
      SELECT * FROM deleted,Rating
      WHERE
        /*  %JoinFKPK(Rating,deleted," = "," AND") */
        Rating.Student_id = deleted.Student_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Student because Rating exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
    /* Student R/24 Present_students_list on parent delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Student"
    CHILD_OWNER="", CHILD_TABLE="Present_students_list"
    P2C_VERB_PHRASE="R/24", C2P_VERB_PHRASE="R/24", 
    FK_CONSTRAINT="R_24", FK_COLUMNS="Student_id" */
    IF EXISTS (
      SELECT * FROM deleted,Present_students_list
      WHERE
        /*  %JoinFKPK(Present_students_list,deleted," = "," AND") */
        Present_students_list.Student_id = deleted.Student_id
    )
    BEGIN
      SELECT @errno  = 30001,
             @errmsg = 'Cannot delete Student because Present_students_list exists.'
      GOTO ERROR
    END

    /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
    /* Group R/7 Student on child delete no action */
    /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Group"
    CHILD_OWNER="", CHILD_TABLE="Student"
    P2C_VERB_PHRASE="R/7", C2P_VERB_PHRASE="R/7", 
    FK_CONSTRAINT="R_7", FK_COLUMNS="Group_id" */
    IF EXISTS (SELECT * FROM deleted,Group
      WHERE
        /* %JoinFKPK(deleted,Group," = "," AND") */
        deleted.Group_id = Group.Group_id AND
        NOT EXISTS (
          SELECT * FROM Student
          WHERE
            /* %JoinFKPK(Student,Group," = "," AND") */
            Student.Group_id = Group.Group_id
        )
    )
    BEGIN
      SELECT @errno  = 30010,
             @errmsg = 'Cannot delete last Student because Group exists.'
      GOTO ERROR
    END


    /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
    RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

CREATE TRIGGER tU_Student ON Student FOR UPDATE AS
/* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
/* UPDATE trigger on Student */
BEGIN
  DECLARE  @NUMROWS int,
           @nullcnt int,
           @validcnt int,
           @insStudent_id integer,
           @errno   int,
           @errmsg  varchar(255)

  SELECT @NUMROWS = @@rowcount
  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Student R/8 Rating on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="0003a500", PARENT_OWNER="", PARENT_TABLE="Student"
    CHILD_OWNER="", CHILD_TABLE="Rating"
    P2C_VERB_PHRASE="R/8", C2P_VERB_PHRASE="R/8", 
    FK_CONSTRAINT="R_8", FK_COLUMNS="Student_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Student_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Rating
      WHERE
        /*  %JoinFKPK(Rating,deleted," = "," AND") */
        Rating.Student_id = deleted.Student_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Student because Rating exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Student R/24 Present_students_list on parent update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Student"
    CHILD_OWNER="", CHILD_TABLE="Present_students_list"
    P2C_VERB_PHRASE="R/24", C2P_VERB_PHRASE="R/24", 
    FK_CONSTRAINT="R_24", FK_COLUMNS="Student_id" */
  IF
    /* %ParentPK(" OR",UPDATE) */
    UPDATE(Student_id)
  BEGIN
    IF EXISTS (
      SELECT * FROM deleted,Present_students_list
      WHERE
        /*  %JoinFKPK(Present_students_list,deleted," = "," AND") */
        Present_students_list.Student_id = deleted.Student_id
    )
    BEGIN
      SELECT @errno  = 30005,
             @errmsg = 'Cannot update Student because Present_students_list exists.'
      GOTO ERROR
    END
  END

  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  /* Group R/7 Student on child update no action */
  /* ERWIN_RELATION:CHECKSUM="00000000", PARENT_OWNER="", PARENT_TABLE="Group"
    CHILD_OWNER="", CHILD_TABLE="Student"
    P2C_VERB_PHRASE="R/7", C2P_VERB_PHRASE="R/7", 
    FK_CONSTRAINT="R_7", FK_COLUMNS="Group_id" */
  IF
    /* %ChildFK(" OR",UPDATE) */
    UPDATE(Group_id)
  BEGIN
    SELECT @nullcnt = 0
    SELECT @validcnt = count(*)
      FROM inserted,Group
        WHERE
          /* %JoinFKPK(inserted,Group) */
          inserted.Group_id = Group.Group_id
    /* %NotnullFK(inserted," IS NULL","select @nullcnt = count(*) from inserted where"," AND") */
    select @nullcnt = count(*) from inserted where
      inserted.Group_id IS NULL
    IF @validcnt + @nullcnt != @NUMROWS
    BEGIN
      SELECT @errno  = 30007,
             @errmsg = 'Cannot update Student because Group does not exist.'
      GOTO ERROR
    END
  END


  /* ERwin Builtin 19 апреля 2017 г. 11:41:56 */
  RETURN
ERROR:
    raiserror @errno @errmsg
    rollback transaction
END
go

