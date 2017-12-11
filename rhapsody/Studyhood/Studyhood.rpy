I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID 23600686-f0fd-4ff5-8b64-6d46d9b6da4f;
	- _myState = 8192;
	- _name = "Studyhood";
	- _objectCreation = "73188311362017929282127";
	- _umlDependencyID = "2515";
	- _lastID = 5;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Default.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Default";
		- _id = GUID cf4e5791-17f7-4f3a-aea9-10c877756e55;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID 0682decb-6a11-4def-b0c2-45b22d2fd8fb;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 3;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID cf4e5791-17f7-4f3a-aea9-10c877756e55;
		}
		{ ISubsystem 
			- fileName = "Server";
			- _id = GUID 3250a69e-d0f7-4a4f-be17-894098063010;
		}
		{ ISubsystem 
			- fileName = "Client";
			- _id = GUID d7a31e5a-a22d-4340-8876-f16ae580f3f8;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ IDiagram 
			- _id = GUID 4a9ea994-607e-4971-942e-de4ce663ee0c;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,151";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "grid_snap";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Main";
			- _objectCreation = "8997511362017929174128";
			- _umlDependencyID = "1902";
			- _lastModifiedTime = "10.19.2017::5:14:4";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 60e178ca-6efa-4045-a1f1-0c6680595332;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 4a9ea994-607e-4971-942e-de4ce663ee0c;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 4;
				{ CGIClass 
					- _id = GUID 7233471d-a79f-4cdd-9f82-f6f4c4c615bb;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID bc801e60-7039-4358-9271-a50ac2b9ba9b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIPackage 
					- _id = GUID e3844afc-edcf-42ad-8ff0-4269c38ea6f0;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Server.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Server";
						- _id = GUID 3250a69e-d0f7-4a4f-be17-894098063010;
					}
					- m_pParent = GUID 7233471d-a79f-4cdd-9f82-f6f4c4c615bb;
					- m_name = { CGIText 
						- m_str = "Server";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.13119 69 193 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID e9a64bb6-315e-4976-91ed-75cfe10a95f2;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Client.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Client";
						- _id = GUID d7a31e5a-a22d-4340-8876-f16ae580f3f8;
					}
					- m_pParent = GUID 7233471d-a79f-4cdd-9f82-f6f4c4c615bb;
					- m_name = { CGIText 
						- m_str = "Client";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.177632 0 0 0.13119 413 193 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID b47270b3-218e-4809-a9a5-d120faa24c3e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "";
						- _name = "Server";
						- _id = GUID 5905e746-d00c-4423-a629-d1fe7029ada8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Server";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID e9a64bb6-315e-4976-91ed-75cfe10a95f2;
					- m_sourceType = 'F';
					- m_pTarget = GUID e3844afc-edcf-42ad-8ff0-4269c38ea6f0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 152 633 ;
					- m_TargetPort = 1115 633 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 7233471d-a79f-4cdd-9f82-f6f4c4c615bb;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID cf4e5791-17f7-4f3a-aea9-10c877756e55;
			}
		}
		{ IDiagram 
			- _id = GUID a4511327-a99a-491a-a032-61183c3dce8c;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Object";
								- Properties = { IRPYRawContainer 
									- size = 9;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Underline@Child.NameCompartment@Name";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "grid_snap";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "\Î\á\ù\à\ÿ \ñ\õ\å\ì\à";
			- _objectCreation = "8997711362017929172128";
			- _umlDependencyID = "1513";
			- _lastModifiedTime = "10.28.2017::6:5:7";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 2e03b924-b2fc-49bd-b316-77e86ef51003;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID a4511327-a99a-491a-a032-61183c3dce8c;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 25;
				{ CGIClass 
					- _id = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID bc801e60-7039-4358-9271-a50ac2b9ba9b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID ec667d8c-5476-4e0e-abff-5aa7321c0a4e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "MainForm";
						- _name = "LoginForm_0";
						- _id = GUID 55cdf76b-a514-4187-a8e2-d3c44433df0b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LoginForm_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID bf974865-c451-429c-ae68-844306229068;
					- m_sourceType = 'F';
					- m_pTarget = GUID a96aea4b-ff47-47d9-83f6-479e1eb5920a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 974 939 ;
					- m_TargetPort = 175 776 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID a002b183-405d-4b59-8e8c-578adbe83bc2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "LoginForm";
						- _name = "GlobalDataModule";
						- _id = GUID 7b296b39-a4d4-48ed-bb86-3e6eeb318d23;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "GlobalDataModule";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a96aea4b-ff47-47d9-83f6-479e1eb5920a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4b22a1ba-def3-47f9-ab6c-ace1dd551fb8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 528 1250 ;
					- m_TargetPort = 424 565 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 9868c782-f816-4454-80f6-b7e7d3047afd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "MainForm";
						- _name = "ActionsListForm_0";
						- _id = GUID 45c8d8af-a997-4eb0-bab6-3d5b14374d1c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "ActionsForm_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID bf974865-c451-429c-ae68-844306229068;
					- m_sourceType = 'F';
					- m_pTarget = GUID 31f09fdb-f20f-48ce-ae80-6fc7d416bf49;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 565 1412 ;
					- m_TargetPort = 493 595 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 2b5e475a-d1b0-4cd3-a9fa-850a711b84d1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "ActionsListForm";
						- _name = "GlobalDataModule";
						- _id = GUID 822070a4-d4b7-47c1-9e85-d04a58c60974;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "GlobalDataModule";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 31f09fdb-f20f-48ce-ae80-6fc7d416bf49;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4b22a1ba-def3-47f9-ab6c-ace1dd551fb8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 989 870 ;
					- m_TargetPort = 177 870 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID f8144303-9421-42c8-b9b3-ccc6180e9e11;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "ActionsListForm";
						- _name = "LessonsListForm";
						- _id = GUID 18c90518-a86d-4e33-8de5-d90ededce3fd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LessonsListForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 31f09fdb-f20f-48ce-ae80-6fc7d416bf49;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7954b7b2-dc1d-4222-ae6c-3e4ce4e92663;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 493 1332 ;
					- m_TargetPort = 156 981 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 328745ba-2954-480a-9b96-736b30608095;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "LessonsListForm";
						- _name = "GlobalDataModule";
						- _id = GUID 937ee770-0069-43df-a3fc-f356e9d11cfd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "GlobalDataModule";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7954b7b2-dc1d-4222-ae6c-3e4ce4e92663;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4b22a1ba-def3-47f9-ab6c-ace1dd551fb8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 397 505 ;
					- m_TargetPort = 424 1405 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 22795d91-ea9a-439a-bcae-2ed35593217f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "LessonsListForm";
						- _name = "LessonInfoForm";
						- _id = GUID 190f475c-381f-4ff3-b917-5e543b969429;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LessonInfoForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7954b7b2-dc1d-4222-ae6c-3e4ce4e92663;
					- m_sourceType = 'F';
					- m_pTarget = GUID 5309b4dd-d475-42f8-99d5-8cddf23a0e13;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 859 762 ;
					- m_TargetPort = 252 890 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 5011e992-d2fe-4473-ad90-3f6be612bd75;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "LessonInfoForm";
						- _name = "PresentListForm_0";
						- _id = GUID 96574201-f04b-46f9-ac7c-5ae4e40e9190;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "PresentListForm_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 5309b4dd-d475-42f8-99d5-8cddf23a0e13;
					- m_sourceType = 'F';
					- m_pTarget = GUID a6ad7a8d-5c16-4f1a-a75c-61c4b28465bf;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 502 472 ;
					- m_TargetPort = 472 1375 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID f63a6f4b-e562-42b2-afb4-5e88b0522b5d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "PresentListForm";
						- _name = "GlobalDataModule";
						- _id = GUID a1f5387e-cefa-4d4f-b1ee-fbe3591eb4ac;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "GlobalDataModule";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a6ad7a8d-5c16-4f1a-a75c-61c4b28465bf;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4b22a1ba-def3-47f9-ab6c-ace1dd551fb8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 122 781 ;
					- m_TargetPort = 968 776 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID bf974865-c451-429c-ae68-844306229068;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "";
						- _name = "MainForm";
						- _id = GUID a739d1c8-2ceb-41ad-9749-a823511e1ef0;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Client::MainForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.195468 0 0 0.110517 302.609 -36.3601 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "MainForm";
							- _name = "EnterSystem_Btn";
							- _id = GUID 8a292c16-410d-406e-8146-313ac4b0487b;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "MainForm";
							- _name = "ChoseAction_Btn";
							- _id = GUID c09aef40-71be-4082-aa68-2bf166a30b66;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "MainForm";
							- _name = "Open_login_form()";
							- _id = GUID 5ac5f76b-d263-4459-9f8f-5cf4728b05c1;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "MainForm";
							- _name = "Open_actions_form()";
							- _id = GUID 76764722-58dd-4bd1-8ccb-8d9253023b86;
						}
					}
				}
				{ CGIClass 
					- _id = GUID a96aea4b-ff47-47d9-83f6-479e1eb5920a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "";
						- _name = "LoginForm";
						- _id = GUID 777cf3a2-3870-4d54-8b58-f6cc94b9d47a;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Client::LoginForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.155807 0 0 0.13458 605.688 -44.2771 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=67%,33%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 4;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Login_Edit";
							- _id = GUID 532f9cd4-126a-4ca6-91d2-b5591dbd1d69;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Password_Edit";
							- _id = GUID 537869d2-c4d3-4415-af75-2a923f95faf9;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Enter_Btn";
							- _id = GUID f7895f2e-75d2-4a3d-b709-0bd066f9d127;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Previous_Btn";
							- _id = GUID b39bb242-c0cb-4660-a2b2-67cdfe8db3a6;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 4;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Log_in_user()";
							- _id = GUID 0e26fb95-f04b-403a-903b-ff0e7b8a3978;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Operation_6()";
							- _id = GUID 3db6f09e-915b-46a3-bcc3-242cf31ca068;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Operation_7()";
							- _id = GUID 009c76aa-bcbc-43f8-882d-308c741bbbb2;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Mark_lesson()";
							- _id = GUID 92b11fbb-3f56-41c0-984a-df33b561c0a8;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 4b22a1ba-def3-47f9-ab6c-ace1dd551fb8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "";
						- _name = "GlobalDataModule";
						- _id = GUID 25337b3c-9bfb-4bae-b18b-8c52a2b1cc81;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Client::GlobalDataModule";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.194523 0 0 0.109625 605.611 156.933 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "TransactionManager";
							- _id = GUID f8f7980b-1841-4b16-bd5f-3c44e5e922af;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 6;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Log_in_user()";
							- _id = GUID df49c871-c5cb-44eb-a617-0f0fb5330421;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Update_login_form()";
							- _id = GUID 01e2fbdd-fd36-43b0-bb7a-23f29d518c55;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Show_actions_list()";
							- _id = GUID 7a042e9d-93c0-405c-bc85-46b37a578508;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_lesson()";
							- _id = GUID 60220377-c72c-4207-9866-11d415a922c1;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_student()";
							- _id = GUID 18dfce0c-9c56-4b9d-81e3-bc2b9ba57713;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Add_lesson_info()";
							- _id = GUID 9ac86a6c-f60a-4218-b053-844cbc2bf697;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 31f09fdb-f20f-48ce-ae80-6fc7d416bf49;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "";
						- _name = "ActionsListForm";
						- _id = GUID f81a0857-135a-4a68-806a-a1e6496b293a;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Client::ActionsListForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.195467 0 0 0.109626 315.609 334.933 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Actions_List";
							- _id = GUID d58343d7-71c7-4ab8-b928-7353c5ebd945;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Choose_Btn";
							- _id = GUID 1fa7bdff-9d39-483e-bfdc-c99eb8434f70;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Previous_Btn";
							- _id = GUID e4cd765f-bc2a-46af-b4c7-ac91bd5308c9;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 8;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Get_actions_list()";
							- _id = GUID ce758e94-b395-4a25-b753-28cb7448a942;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Open_lessons_form()";
							- _id = GUID aafab52a-4de4-4ffd-a79c-af67f7bc174f;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Show_actions_list()";
							- _id = GUID 8b6c286e-8dec-40cd-baca-4804117c3baf;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Operation_8()";
							- _id = GUID e4e4f65b-c43e-4ded-aaf1-3f09ffe33979;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Open_actions_list_form()";
							- _id = GUID f087fded-55a8-4fc0-9c17-539ff092a7e4;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Choose_action()";
							- _id = GUID ee3ec234-6c5d-43aa-b0fe-c35d90edd630;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Update_action_form()";
							- _id = GUID 1c7c63ae-03f2-4855-816a-9ad4a700ea78;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Synchronize_lessons_list()";
							- _id = GUID 0f0a2458-4039-42af-b828-d75724170546;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 7954b7b2-dc1d-4222-ae6c-3e4ce4e92663;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "";
						- _name = "LessonsListForm";
						- _id = GUID ecbacf4e-025e-4018-acc6-a7b0b29e15a5;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Client::LessonsListForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.207743 0 0 0.159537 605.585 318.513 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Lessons_Table";
							- _id = GUID 2d1308c2-4656-4a1b-b26b-6e71c74f3077;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Choose_Btn";
							- _id = GUID 689cb4a4-e7e0-498b-87d4-5b17dbc1e0a5;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Previous_Btn";
							- _id = GUID 1ccac373-5fe9-4330-a3d5-f7caf6060ec6;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 5;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Synchronize_lessons()";
							- _id = GUID 32acebcd-5a7f-4123-931f-3704bcd69e39;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Get_lesson()";
							- _id = GUID 4d0b0e55-e7a3-4d64-801d-4765811a146f;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Choose_lesson()";
							- _id = GUID e3690f9a-fbf9-48b1-8424-e931a1643876;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Open_lessons_list_form()";
							- _id = GUID 63adfea9-1083-49a1-8894-820c3c69f0bd;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Update_lessons_list_form()";
							- _id = GUID 8b4ad549-8dc3-45b6-8c34-ab3cc7e8a37f;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 5309b4dd-d475-42f8-99d5-8cddf23a0e13;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "";
						- _name = "LessonInfoForm";
						- _id = GUID 1f0918ed-1d67-49c9-82d1-efeaf86c515b;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Client::LessonInfoForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.220019 0 0 0.221033 907.56 257.28 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=72%,28%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 7;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Date_Label";
							- _id = GUID 11038464-b67b-4b92-a26c-d4c2bedcbf7a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Time_Label";
							- _id = GUID 46faeda4-820e-46c7-9c73-8c0ccd2ef362;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Subject_Label";
							- _id = GUID a522eb39-dd1e-4a85-87b8-86556b672b11;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Groups_Label";
							- _id = GUID 1ebb86d5-b8bb-48d3-ac09-34c9ae5fff1c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Room_Label";
							- _id = GUID 85e12b84-622b-4033-80b3-3577702e4ea8;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Type_Label";
							- _id = GUID 3199074d-788e-4b9f-a2b9-7f9ebbdef338;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "ShowPresentList_Btn";
							- _id = GUID d8c1d5e5-d852-4ff9-8a2e-2193c810f141;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 6;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Open_present_list_form()";
							- _id = GUID e8d6d61c-cf88-4e55-aa2c-ba078248b4e9;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Add_lesson_info()";
							- _id = GUID e3a2fd68-71b3-42d7-b510-2c3d813969bf;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Open_lesson_form()";
							- _id = GUID f16bf928-f740-40dc-92ec-ead70bd2363c;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Set_lesson_info()";
							- _id = GUID 4df1eba5-4a6a-4e4a-8147-85166a39c78f;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Mark_present()";
							- _id = GUID d190ce5a-60c0-4f6f-9139-a9be45259497;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Close_lesson_info_form()";
							- _id = GUID 95579811-cfea-471b-97d3-9ab134bdc3ed;
						}
					}
				}
				{ CGIClass 
					- _id = GUID a6ad7a8d-5c16-4f1a-a75c-61c4b28465bf;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "";
						- _name = "PresentListForm";
						- _id = GUID ceb79c97-88f8-4cb2-aaed-4dc3ed248ee7;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Client::PresentListForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.234183 0 0 0.196079 907.532 -64.5098 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=61%,39%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 5;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Students_Table";
							- _id = GUID 5c491c23-c732-4750-944a-562c6f06b5af;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Mark_Btn";
							- _id = GUID 56caa2b1-55e3-409c-94a7-dec5c4e0fbfe;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Remove_Btn";
							- _id = GUID 97da951c-5ea3-4052-abe3-895fc019ba05;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Save_Btn";
							- _id = GUID 218ca302-cef9-46b2-8da4-4be76ce46211;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Cancel_Btn";
							- _id = GUID cbf60ad3-21c0-4ca1-a48f-2150e192ae7e;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 5;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Synchronize_students_list()";
							- _id = GUID da68603f-7b4f-4069-922a-4874692863ec;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Mark_student()";
							- _id = GUID bc2d3978-4aa1-4e9f-9dd6-422fcb0b9c20;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Unmark_student()";
							- _id = GUID 726e45cc-3b6e-4fa6-9f72-2b24d248839d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Open_present_list_form()";
							- _id = GUID cbe79ce3-0f04-4baa-bc44-55491893bf9b;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Close_present_list_form()";
							- _id = GUID d72d07f7-c6d8-4020-9477-9f656e92a7c8;
						}
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID b1e3e904-7ccd-4180-a3fb-69b7ffe1bbea;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Server.sbs";
						- _subsystem = "Server";
						- _class = "Lesson";
						- _name = "itsStudent";
						- _id = GUID 0583eab6-a730-44d2-ab32-94ba7cc60391;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID de88f250-04b4-4a07-9b56-e25d4ba35af5;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3469f91a-ac0b-4d7a-aef2-1d270b54fa54;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 158 467 ;
					- m_TargetPort = 181 1362 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 51789c78-9c5b-42bc-b743-7ba238e60d37;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Server.sbs";
						- _subsystem = "Server";
						- _class = "Teacher";
						- _name = "itsLesson_2";
						- _id = GUID 406bfc13-5b6c-4c26-8a00-35dfe40be411;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID f987f747-0385-4462-bbf4-6b2bb6cb19ec;
					- m_sourceType = 'F';
					- m_pTarget = GUID de88f250-04b4-4a07-9b56-e25d4ba35af5;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 195 464 ;
					- m_TargetPort = 158 1412 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIClass 
					- _id = GUID 3469f91a-ac0b-4d7a-aef2-1d270b54fa54;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Server.sbs";
						- _subsystem = "Server";
						- _class = "";
						- _name = "Student";
						- _id = GUID 737f6174-ce15-4b7e-806e-196aaeb3d151;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Server::Student";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.172804 0 0 0.101604 -0.345604 -33.4278 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Student";
							- _name = "FIO";
							- _id = GUID fd04ec5c-881b-4229-a99d-42887f000a4f;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Student";
							- _name = "GroupID";
							- _id = GUID 6e6b93d4-536e-4f02-a1d6-3bb108a015de;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Student";
							- _name = "Get_student()";
							- _id = GUID 11bb3ed6-a197-4577-a5ef-b55c164240f2;
						}
					}
				}
				{ CGIClass 
					- _id = GUID de88f250-04b4-4a07-9b56-e25d4ba35af5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Server.sbs";
						- _subsystem = "Server";
						- _class = "";
						- _name = "Lesson";
						- _id = GUID 610478f1-91f0-427c-9fe1-d76dcd112728;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Server::Lesson";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.179415 0 0 0.101604 -0.358833 131.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 6;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Date";
							- _id = GUID b28af960-1259-4c3a-b66d-ed845d3bcf9d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Subject";
							- _id = GUID 54839817-1394-4d41-a4fb-ee295dd4a4f5;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Type";
							- _id = GUID 458ee66d-03d3-4627-b0e5-a689b67a15ce;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Groups";
							- _id = GUID e310d37f-7952-4d24-b7a9-1ec41f455f4a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Room";
							- _id = GUID 0d17965f-83b9-4477-9110-035925a39317;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Teacher";
							- _id = GUID 4d74a166-0f40-490d-a754-273fa536c745;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Add_lesson_info()";
							- _id = GUID 1e4fb02f-bdb4-48ac-b9bc-b6ce43ca67fe;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Mark_present()";
							- _id = GUID 7a883e3b-68ea-48dc-9ec5-4d73b642861d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Get_lesson()";
							- _id = GUID cda49f6c-19dc-4023-9c2d-6916d171be6e;
						}
					}
				}
				{ CGIClass 
					- _id = GUID f987f747-0385-4462-bbf4-6b2bb6cb19ec;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Server.sbs";
						- _subsystem = "Server";
						- _class = "";
						- _name = "Teacher";
						- _id = GUID f0e9ef18-da13-41bc-b3fe-cb86b1ebbd0a;
					}
					- m_pParent = GUID 4c80644a-656e-4930-8322-940570062085;
					- m_name = { CGIText 
						- m_str = "Server::Teacher";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.145421 0 0 0.133689 -0.29081 286.016 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=47%,53%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Teacher";
							- _name = "FIO";
							- _id = GUID 4ceec756-4fc4-421e-900f-90a30787781a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Teacher";
							- _name = "Job";
							- _id = GUID 4e0f9b80-37bb-4fac-8517-a3c76e229971;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Teacher";
							- _name = "Mark_lesson()";
							- _id = GUID 00c08644-d967-4558-9d45-10d4ffbd3e74;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID 750241b4-6df4-4f77-909e-952e54c2f281;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "GlobalDataModule";
						- _name = "Student";
						- _id = GUID 8dab9ef1-3a81-4181-b948-e390d45dcfe8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Student";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4b22a1ba-def3-47f9-ab6c-ace1dd551fb8;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3469f91a-ac0b-4d7a-aef2-1d270b54fa54;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 69 831 ;
					- m_TargetPort = 957 1156 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID aa68a7ef-4f41-40d4-bc36-975d448b98c0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "GlobalDataModule";
						- _name = "Lesson";
						- _id = GUID 228d29d8-14ac-48ff-a1d0-596607e853dc;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Lesson";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4b22a1ba-def3-47f9-ab6c-ace1dd551fb8;
					- m_sourceType = 'F';
					- m_pTarget = GUID de88f250-04b4-4a07-9b56-e25d4ba35af5;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 69 949 ;
					- m_TargetPort = 777 742 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 6e876140-aac6-48ee-af62-154dfe634206;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Client.sbs";
						- _subsystem = "Client";
						- _class = "GlobalDataModule";
						- _name = "Teacher";
						- _id = GUID b3fcd586-4340-4580-8c54-2f2e819a18af;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Teacher";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4b22a1ba-def3-47f9-ab6c-ace1dd551fb8;
					- m_sourceType = 'F';
					- m_pTarget = GUID f987f747-0385-4462-bbf4-6b2bb6cb19ec;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 69 1077 ;
					- m_TargetPort = 552 606 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 4c80644a-656e-4930-8322-940570062085;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID cf4e5791-17f7-4f3a-aea9-10c877756e55;
			}
		}
	}
	- MSCS = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IMSC 
			- _id = GUID cc30ced3-9f80-4c82-9d15-c77f515d80f8;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CreateMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "EnvironmentLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ReplyMessage";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 3;
									- value = 
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Add_lesson_info";
			- _objectCreation = "8997911362017929170128";
			- _umlDependencyID = "3056";
			- _lastModifiedTime = "10.28.2017::6:5:22";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID b947a060-573a-41cb-9120-2d027a688cfa;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID cc30ced3-9f80-4c82-9d15-c77f515d80f8;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 59;
				{ CGIBox 
					- _id = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID c0379c1b-35a0-4bd5-a215-568e92376151;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID dedd2c0a-c9ed-4fb8-930f-3f12fae542d6;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 1df0b941-f3b3-42b4-b0d4-1e8058496769;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü:Teacher";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.32292 0 0 0.0327951 0 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 50000  96 50000  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID d0b60070-1c3b-4e2a-b6d2-16b639a144c9;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID e77fb521-941d-409f-8f67-d9ad9f00941c;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ô\î\ð\ì\à \à\â\ò\î\ð\è\ç\à\ö\è\è:LoginForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.07292 0 0 0.0328706 142 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ì\å\í\å\ä\æ\å\ð \ò\ð\à\í\ç\à\ê\ö\è\é:GlobalDataModule";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.3125 0 0 0.0328706 300 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ñ\ï\è\ñ\î\ê \ä\å\é\ñ\ò\â\è\é:ActionsListForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.15625 0 0 0.0328706 465 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ñ\ï\è\ñ\î\ê \ç\à\í\ÿ\ò\è\é:LessonsListForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.17708 0 0 0.0328706 595 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 23dcbff2-bcff-4e12-858a-5c5e990315ef;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 30229201-2f7e-4bab-ac3d-46b768e4bf51;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ç\à\í\ÿ\ò\è\å:Lesson";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0328706 730 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ä\à\í\í\û\å \ç\à\í\ÿ\ò\è\ÿ:LessonInfoForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.03125 0 0 0.0328706 843 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ñ\ï\è\ñ\î\ê \ï\ð\è\ñ\ó\ò\ñ\ò\â\ó\þ\ù\è\õ:PresentListForm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0328706 962 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 4787e118-b055-4b31-bca4-b6376b9f9164;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 8818da5d-b300-467c-a9bc-4387fb6b290d;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ñ\ï\è\ñ\î\ê \ñ\ò\ó\ä\å\í\ò\î\â:Student";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0328706 1079 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 4d1dc794-62e0-4ae5-afcf-8f02d9e198c7;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 6455d908-220c-416a-9a4a-693a628e41e2;
					}
					- m_pParent = GUID dedd2c0a-c9ed-4fb8-930f-3f12fae542d6;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.755905 0 0 30.4923 43.0866 3323.67 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9f27505b-5eae-486c-b677-dfa1a93c72d1;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID fefd3f91-0624-4889-be9e-ea6a02c65a13;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 53184907-3e44-4f48-a59b-22043416bfc5;
					}
					- m_pParent = GUID d0b60070-1c3b-4e2a-b6d2-16b639a144c9;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.932039 0 0 30.4222 41.9418 3316.02 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9f27505b-5eae-486c-b677-dfa1a93c72d1;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID eff9c99d-f3a6-47b5-917d-3265235fdae3;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 31e0967b-f1a2-4f1e-a001-b6a32374a2fe;
					}
					- m_pParent = GUID d0b60070-1c3b-4e2a-b6d2-16b639a144c9;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.932039 0 0 82.816 41.9418 5323.89 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID a98001c0-5e8b-499c-9bda-508c65f2fec0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID e93b2a50-67a1-40c7-a0d6-f0bf3944ff43;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c32c491c-8b01-4292-a782-155820d14d8c;
					}
					- m_pParent = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.761905 0 0 30.4222 43.4286 5323.89 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID a98001c0-5e8b-499c-9bda-508c65f2fec0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 11dc6346-eecf-4aba-b16b-6dbd7e81e2fe;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID d2c722b7-24cc-46f8-8bef-332aed24a0b4;
					}
					- m_pParent = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.761905 0 0 54.929 43.4286 7210.07 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID edfd0fc7-327b-43a6-8925-43457499c6b2;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID ff71f2cd-76de-4d34-9855-94df084450e7;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 7e7f13db-0ea7-4e1c-8409-ca11136c693d;
					}
					- m_pParent = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.864865 0 0 38.0277 42.3784 8092.33 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9b4080c5-cf93-4dfc-86fe-95c0bde65f5e;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID c1b8431a-fbc1-4af2-aad0-4bbff6351244;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 7ed9a8fc-4118-4f6a-baa8-60db72d99030;
					}
					- m_pParent = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.864865 0 0 183.378 42.3784 10708.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID c240dd1c-9ff8-46ab-9240-87f02f79f299;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 68544774-3c38-4b6d-b2d7-08119b03739c;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 662e301a-95fc-4ba9-86af-ecf6e96c55f3;
					}
					- m_pParent = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.761905 0 0 76.9005 43.4286 16215 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 89434a10-4b34-4a41-af87-3f31c3414e35;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 9c751ff4-5bd9-4387-bbe6-a3a32605036e;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 568a0bed-aa00-4b9f-9703-9cf47d0e24ce;
					}
					- m_pParent = GUID 23dcbff2-bcff-4e12-858a-5c5e990315ef;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 30.4223 42 17888.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 06667a62-7cdd-44cf-86c7-8c1287defb33;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 129e3f25-a16b-4804-adf2-572b324842e8;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 59540170-899d-40af-848d-712fd225b197;
					}
					- m_pParent = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.864865 0 0 30.4222 42.3784 19591.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8852b7d1-af86-4123-b458-283a27231546;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 552204b0-37e4-48ea-b560-0dba19313b4d;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID ad1ec94a-25ef-4915-a31f-42db8c31c019;
					}
					- m_pParent = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.84956 0 0 34.6476 42.478 19591.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8852b7d1-af86-4123-b458-283a27231546;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 950cacc4-3a78-4ce9-81ba-485962a8a989;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 75d9e189-05e8-4f1f-80b1-55581cdc8a36;
					}
					- m_pParent = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.84956 0 0 119.999 42.478 22086.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 7da8e1b8-08c3-481d-b91e-63f12aae3471;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 38bddca4-0f1e-4c92-b0fa-5e43d6248fd7;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 14434c37-5cfe-4c09-a9e3-51c8b391d687;
					}
					- m_pParent = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.969697 0 0 36.3377 41.6969 25311.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 28de914a-dc3b-4380-bc77-539f289253d6;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 6b5cdf3c-1ab5-4f28-a65f-0a5c7a3e579f;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 41b3450e-f078-4e5f-9c31-444c4f1436c1;
					}
					- m_pParent = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.969697 0 0 107.323 41.6969 27197.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9cb6c1ba-dd95-4544-a614-5777d628e50a;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 64594207-7920-4617-9614-248068dc58b1;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 1e8f4d1c-b739-486c-9d48-ac812efea75a;
					}
					- m_pParent = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 166.477 42 29965.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b01b5613-3769-4996-9d3c-99cd9d2023e0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 26634ec7-19e3-4cd1-bbd7-9db24a9947dc;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID e3be40ce-1cab-4555-8b36-aa2af87e6b80;
					}
					- m_pParent = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.761905 0 0 71.8303 43.4286 34863.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID fffaf61e-eeb2-4af5-9a01-7739de47a68a;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 5883c7d1-f91d-4857-864e-10e1861fef90;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 20f7de05-4c14-4945-977b-b98a83cedbb3;
					}
					- m_pParent = GUID 4787e118-b055-4b31-bca4-b6376b9f9164;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 30.4223 42 36354.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8f758c41-c6a1-44ba-98d1-a4f1e7f79e3a;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID d9536d55-2b31-4256-8a5d-d8d8ecce2894;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 32387afc-7418-4333-8eea-130014ab7cfa;
					}
					- m_pParent = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 30.4223 42 37814.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID edb6c9bf-a93d-4361-b621-2bf3d19a1bef;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 31662c90-23b1-4208-8ef2-01b5a93d764a;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID f0b19860-f4b9-442f-b4ef-cf9132a19080;
					}
					- m_pParent = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.969697 0 0 56.6193 41.6969 37814.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID edb6c9bf-a93d-4361-b621-2bf3d19a1bef;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 71f728bf-8593-4895-a6ea-028a7409846f;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 640e4a8a-aec4-4c62-8219-3ff6d7f817db;
					}
					- m_pParent = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.761905 0 0 114.084 43.4286 38757.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 29083307-f366-4816-9181-98dca4f69049;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID f7d5b9c6-627f-497c-aa79-703c9ae9f6c2;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 43fed37a-3342-4088-8187-17175c081413;
					}
					- m_pParent = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 0.969697 0 0 57.4643 41.6969 40461.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID df9011b7-91cc-4ac2-ace9-a5cebd54a1c0;
				}
				{ CGIMscMessage 
					- _id = GUID c240dd1c-9ff8-46ab-9240-87f02f79f299;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d8d3664c-df5b-4833-bcbf-6e62729cd618;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_actions_list_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 551 341  551 402  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 8853 ;
					- m_TargetPort = 48 10709 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID c1b8431a-fbc1-4af2-aad0-4bbff6351244;
				}
				{ CGIMscMessage 
					- _id = GUID 8852b7d1-af86-4123-b458-283a27231546;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 605d9c34-621f-4a88-a69d-455a4c3ab246;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_lessons_list_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -68 -8  125 -8  125 11  -68 11  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 589 665 ;
						- m_nHorizontalSpacing = -5;
						- m_nVerticalSpacing = 1;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 19592 ;
					- m_TargetPort = 48 19592 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 129e3f25-a16b-4804-adf2-572b324842e8;
					- m_pTargetExec = GUID 552204b0-37e4-48ea-b560-0dba19313b4d;
				}
				{ CGIMscMessage 
					- _id = GUID a98001c0-5e8b-499c-9bda-508c65f2fec0;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 9f4e4e93-519b-4f26-a933-64b77b4a1146;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Log_in_user()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d0b60070-1c3b-4e2a-b6d2-16b639a144c9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 5324 ;
					- m_TargetPort = 48 5324 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID eff9c99d-f3a6-47b5-917d-3265235fdae3;
					- m_pTargetExec = GUID e93b2a50-67a1-40c7-a0d6-f0bf3944ff43;
				}
				{ CGIMscMessage 
					- _id = GUID edfd0fc7-327b-43a6-8925-43457499c6b2;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID aceb84e0-74f1-4641-bdac-47d8cbd24bbd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Show_actions_list()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d0b60070-1c3b-4e2a-b6d2-16b639a144c9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 7210 ;
					- m_TargetPort = 48 7210 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 11dc6346-eecf-4aba-b16b-6dbd7e81e2fe;
				}
				{ CGIMscMessage 
					- _id = GUID dab82f8b-5e39-4531-8ae1-88833a759169;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 68e38887-aa8b-4a29-b0d1-4a737f0019e0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_present_list_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_sourceType = 'F';
					- m_pTarget = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1040 1055  1040 1075  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 30574 ;
					- m_TargetPort = 48 31183 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID df9011b7-91cc-4ac2-ace9-a5cebd54a1c0;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 257abefd-7106-414b-a269-7d4de99051b8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Close_lesson_info_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 40462 ;
					- m_TargetPort = 48 40462 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID f7d5b9c6-627f-497c-aa79-703c9ae9f6c2;
				}
				{ CGIMscMessage 
					- _id = GUID cb1c7825-490f-4953-90de-10fecf7c239b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 963c6239-69f9-4dbb-aadf-d94c8379bb79;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_lesson(Lesson)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -36 -9  150 -9  150 10  -36 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 694 792 ;
						- m_nHorizontalSpacing = 1;
						- m_nVerticalSpacing = -1;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 681 827  681 847  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 23638 ;
					- m_TargetPort = 48 24247 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 708d8cf1-a59f-44ce-8ca1-2aa6930648fe;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a30e5764-c08d-42b1-b268-9dd2f4eb2f38;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Set_lesson_info()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_sourceType = 'F';
					- m_pTarget = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 923 977  923 999  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 28201 ;
					- m_TargetPort = 48 28871 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 33b39ae3-e984-40b8-8824-f67dcdcaa4f6;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 8959a2d9-14d8-45b6-924c-717c244141db;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_lessons_list_form(Info)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 42257 ;
					- m_TargetPort = 48 42257 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID b01b5613-3769-4996-9d3c-99cd9d2023e0;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID ffae52ad-ab99-4ca7-9093-13ac206e0200;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_present_list_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_sourceType = 'F';
					- m_pTarget = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 29966 ;
					- m_TargetPort = 48 29966 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 64594207-7920-4617-9614-248068dc58b1;
				}
				{ CGIMscMessage 
					- _id = GUID e1eb036e-5ff1-43c4-bcb7-63a5f8f232db;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4666f6a6-20e4-476d-aa32-968b58bb2b85;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_action_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 551 483  551 516  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 13173 ;
					- m_TargetPort = 48 14177 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 9f27505b-5eae-486c-b677-dfa1a93c72d1;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 1162968a-36fc-4c53-b888-49f3c2388ad9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Mark_lesson()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID dedd2c0a-c9ed-4fb8-930f-3f12fae542d6;
					- m_sourceType = 'F';
					- m_pTarget = GUID d0b60070-1c3b-4e2a-b6d2-16b639a144c9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 3324 ;
					- m_TargetPort = 48 3316 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 4d1dc794-62e0-4ae5-afcf-8f02d9e198c7;
					- m_pTargetExec = GUID fefd3f91-0624-4889-be9e-ea6a02c65a13;
				}
				{ CGIMscMessage 
					- _id = GUID 9b4080c5-cf93-4dfc-86fe-95c0bde65f5e;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 51a923f4-a441-4a67-9cbd-624010c16afd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Show_actions_list()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 8092 ;
					- m_TargetPort = 48 8092 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID ff71f2cd-76de-4d34-9855-94df084450e7;
				}
				{ CGIMscMessage 
					- _id = GUID e544a2a4-b271-4f74-a624-99b9c4224526;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 27a3608b-9825-4962-ad28-15f7bff80130;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_action(\"mark_lesson\")";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 551 432  551 452  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 11621 ;
					- m_TargetPort = 48 12230 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID f6d41746-0e53-45f7-8bce-cbbf4b8747b0;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c6eaae66-6ddc-4ee5-9a5e-a65b1453a718;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_login_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_sourceType = 'F';
					- m_pTarget = GUID d0b60070-1c3b-4e2a-b6d2-16b639a144c9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 6145 ;
					- m_TargetPort = 48 6145 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 9cb6c1ba-dd95-4544-a614-5777d628e50a;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e3b84458-9107-4206-b873-1bc0209added;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_lesson_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_sourceType = 'F';
					- m_pTarget = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 923 905  923 944  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 26011 ;
					- m_TargetPort = 48 27198 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 6b5cdf3c-1ab5-4f28-a65f-0a5c7a3e579f;
				}
				{ CGIMscMessage 
					- _id = GUID b67c26fa-1361-4563-8198-4aa4b0d80b0a;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID dcd6eb35-cfb9-41da-8f5c-843027755416;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Close_present_list_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_sourceType = 'F';
					- m_pTarget = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 41435 ;
					- m_TargetPort = 48 41435 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 1b04f57f-7536-4e36-b31c-e80353bc4413;
				}
				{ CGIMscMessage 
					- _id = GUID 29083307-f366-4816-9181-98dca4f69049;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a3c624f8-c4a1-4765-a76d-ef48df7de367;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Add_lesson_info(Info)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 38758 ;
					- m_TargetPort = 48 38758 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 71f728bf-8593-4895-a6ea-028a7409846f;
				}
				{ CGIMscMessage 
					- _id = GUID 89434a10-4b34-4a41-af87-3f31c3414e35;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 0ebaa497-ea05-4001-b219-397b1950a512;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_lesson(Lesson)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 16215 ;
					- m_TargetPort = 48 16215 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 68544774-3c38-4b6d-b2d7-08119b03739c;
				}
				{ CGIMscMessage 
					- _id = GUID fffaf61e-eeb2-4af5-9a01-7739de47a68a;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5dc1048b-51e6-47ca-ab35-4fcdcbcb4240;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_student(Student)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 34864 ;
					- m_TargetPort = 48 34864 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 26634ec7-19e3-4cd1-bbd7-9db24a9947dc;
				}
				{ CGIMscMessage 
					- _id = GUID 06667a62-7cdd-44cf-86c7-8c1287defb33;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID b0940618-1f47-48db-b124-0bf8afad9f5d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_lesson(Lesson)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 23dcbff2-bcff-4e12-858a-5c5e990315ef;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 17888 ;
					- m_TargetPort = 48 17888 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 9c751ff4-5bd9-4387-bbe6-a3a32605036e;
				}
				{ CGIMscMessage 
					- _id = GUID ea24e25d-0a16-44af-8f11-7ba0257f8df7;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 06152e2e-256b-4842-a336-d3c68714f3e8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Synchronize_students_list()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_sourceType = 'F';
					- m_pTarget = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1040 1135  1040 1155  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 33008 ;
					- m_TargetPort = 48 33617 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 28de914a-dc3b-4380-bc77-539f289253d6;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 891054c3-2805-4899-8dbd-23a2b48b382e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_lesson_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 25311 ;
					- m_TargetPort = 48 25311 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 38bddca4-0f1e-4c92-b0fa-5e43d6248fd7;
				}
				{ CGIMscMessage 
					- _id = GUID 8f758c41-c6a1-44ba-98d1-a4f1e7f79e3a;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID fe91bbfe-d9c3-4d0e-844a-3ce7f6c999bd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_student(Student)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2f58b8df-b247-4dd4-9df0-5ad38aefadd9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4787e118-b055-4b31-bca4-b6376b9f9164;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 36355 ;
					- m_TargetPort = 48 36355 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 5883c7d1-f91d-4857-864e-10e1861fef90;
				}
				{ CGIMscMessage 
					- _id = GUID edb6c9bf-a93d-4361-b621-2bf3d19a1bef;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID cf85f063-c8b3-4ce2-af50-9be1b5981cf1;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Mark_present()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_sourceType = 'F';
					- m_pTarget = GUID 99d6b26d-8d69-4e96-8f10-ba11e63ee8a4;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 37815 ;
					- m_TargetPort = 48 37815 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID d9536d55-2b31-4256-8a5d-d8d8ecce2894;
					- m_pTargetExec = GUID 31662c90-23b1-4208-8ef2-01b5a93d764a;
				}
				{ CGIMscMessage 
					- _id = GUID 8a6b5ec4-034a-47aa-b6bc-273c3ca69a2a;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 078c692b-c4ad-47e9-ad73-40560c1ba2dc;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Synchronize_lessons_list()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 9fd72b81-3752-47c6-8898-07412903bf5b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 551 542  551 563  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 14968 ;
					- m_TargetPort = 48 15607 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 7da8e1b8-08c3-481d-b91e-63f12aae3471;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 67947061-feae-482f-aef7-f497aa0a11cd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_lessons_list_form()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a025aff-1942-40de-935b-64d9e8830ef1;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 681 715  681 776  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 20231 ;
					- m_TargetPort = 48 22087 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 950cacc4-3a78-4ce9-81ba-485962a8a989;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 1b04f57f-7536-4e36-b31c-e80353bc4413;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID dd6abadc-5d7b-46e4-a6fc-750f1671f4c2;
					}
					- m_pParent = GUID fadbfe55-2f11-4278-aa0d-fa6fa624a6a3;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 30.4223 42 41435.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b67c26fa-1361-4563-8198-4aa4b0d80b0a;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID cf4e5791-17f7-4f3a-aea9-10c877756e55;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID c0379c1b-35a0-4bd5-a215-568e92376151;
				- _objectCreation = "8998111362017929168128";
				- _umlDependencyID = "1513";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 9;
					- value = 
					{ IClassifierRole 
						- _id = GUID 1df0b941-f3b3-42b4-b0d4-1e8058496769;
						- _name = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _objectCreation = "8998311362017929166128";
						- _umlDependencyID = "1513";
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "";
							- _name = "Teacher";
							- _id = GUID f0e9ef18-da13-41bc-b3fe-cb86b1ebbd0a;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID e77fb521-941d-409f-8f67-d9ad9f00941c;
						- _name = "\Ô\î\ð\ì\à \à\â\ò\î\ð\è\ç\à\ö\è\è";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e0\\'e2\\'f2\\'ee\\'f0\\'e8\\'e7\\'e0\\'f6\\'e8\\'e8\\par
}
";
						- _objectCreation = "8998511362017929164128";
						- _umlDependencyID = "1513";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "LoginForm";
							- _id = GUID 777cf3a2-3870-4d54-8b58-f6cc94b9d47a;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						- _name = "\Ì\å\í\å\ä\æ\å\ð \ò\ð\à\í\ç\à\ê\ö\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'cc\\'ee\\'e4\\'f3\\'eb\\'fc \\'e3\\'eb\\'ee\\'e1\\'e0\\'eb\\'fc\\'ed\\'fb\\'f5 \\'e4\\'e0\\'ed\\'ed\\'fb\\'f5\\par
}
";
						- _objectCreation = "8998711362017929162128";
						- _umlDependencyID = "1513";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "GlobalDataModule";
							- _id = GUID 25337b3c-9bfb-4bae-b18b-8c52a2b1cc81;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						- _name = "\Ñ\ï\è\ñ\î\ê \ä\å\é\ñ\ò\â\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e2\\'fb\\'e1\\'ee\\'f0\\'e0 \\'e4\\'e5\\'e9\\'f1\\'f2\\'e2\\'e8\\'e9\\par
}
";
						- _objectCreation = "8998911362017929160128";
						- _umlDependencyID = "1513";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "ActionsListForm";
							- _id = GUID f81a0857-135a-4a68-806a-a1e6496b293a;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
						- _name = "\Ñ\ï\è\ñ\î\ê \ç\à\í\ÿ\ò\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'ee\\'f2\\'ee\\'e1\\'f0\\'e0\\'e6\\'e5\\'ed\\'e8\\'ff \\'f1\\'ef\\'e8\\'f1\\'ea\\'e0 \\'e7\\'e0\\'ed\\'ff\\'f2\\'e8\\'e9\\par
}
";
						- _objectCreation = "8999111362017929158128";
						- _umlDependencyID = "1513";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "LessonsListForm";
							- _id = GUID ecbacf4e-025e-4018-acc6-a7b0b29e15a5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 30229201-2f7e-4bab-ac3d-46b768e4bf51;
						- _name = "\Ç\à\í\ÿ\ò\è\å";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'c7\\'e0\\'ed\\'ff\\'f2\\'e8\\'e5\\par
}
";
						- _objectCreation = "8999311362017929156128";
						- _umlDependencyID = "1513";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "";
							- _name = "Lesson";
							- _id = GUID 610478f1-91f0-427c-9fe1-d76dcd112728;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						- _name = "\Ä\à\í\í\û\å \ç\à\í\ÿ\ò\è\ÿ";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'ee\\'f2\\'ee\\'e1\\'f0\\'e0\\'e6\\'e5\\'ed\\'e8\\'ff \\'e7\\'e0\\'ed\\'ff\\'f2\\'e8\\'ff\\par
}
";
						- _objectCreation = "8999511362017929154128";
						- _umlDependencyID = "1513";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "LessonInfoForm";
							- _id = GUID 1f0918ed-1d67-49c9-82d1-efeaf86c515b;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						- _name = "\Ñ\ï\è\ñ\î\ê \ï\ð\è\ñ\ó\ò\ñ\ò\â\ó\þ\ù\è\õ";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e2\\'fb\\'e1\\'ee\\'f0\\'e0 \\'ef\\'f0\\'e8\\'f1\\'f3\\'f2\\'f1\\'f2\\'e2\\'f3\\'fe\\'f9\\'e8\\'f5\\par
}
";
						- _objectCreation = "8999711362017929152128";
						- _umlDependencyID = "1513";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "PresentListForm";
							- _id = GUID ceb79c97-88f8-4cb2-aaed-4dc3ed248ee7;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 8818da5d-b300-467c-a9bc-4387fb6b290d;
						- _name = "\Ñ\ï\è\ñ\î\ê \ñ\ò\ó\ä\å\í\ò\î\â";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d1\\'f2\\'f3\\'e4\\'e5\\'ed\\'f2\\par
}
";
						- _objectCreation = "8999911362017929150128";
						- _umlDependencyID = "1513";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "";
							- _name = "Student";
							- _id = GUID 737f6174-ce15-4b7e-806e-196aaeb3d151;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 27;
					- value = 
					{ IMessage 
						- _id = GUID 1162968a-36fc-4c53-b888-49f3c2388ad9;
						- _name = "Mark_lesson";
						- _objectCreation = "81000111362017929148128";
						- _umlDependencyID = "2684";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e77fb521-941d-409f-8f67-d9ad9f00941c;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1df0b941-f3b3-42b4-b0d4-1e8058496769;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Mark_lesson()";
							- _id = GUID 92b11fbb-3f56-41c0-984a-df33b561c0a8;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 53184907-3e44-4f48-a59b-22043416bfc5;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 6455d908-220c-416a-9a4a-693a628e41e2;
						}
					}
					{ IMessage 
						- _id = GUID 9f4e4e93-519b-4f26-a933-64b77b4a1146;
						- _name = "Log_in_user";
						- _objectCreation = "81000311362017929146128";
						- _umlDependencyID = "2676";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e77fb521-941d-409f-8f67-d9ad9f00941c;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Log_in_user()";
							- _id = GUID df49c871-c5cb-44eb-a617-0f0fb5330421;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c32c491c-8b01-4292-a782-155820d14d8c;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 31e0967b-f1a2-4f1e-a001-b6a32374a2fe;
						}
					}
					{ IMessage 
						- _id = GUID c6eaae66-6ddc-4ee5-9a5e-a65b1453a718;
						- _name = "Update_login_form";
						- _objectCreation = "81000511362017929144128";
						- _umlDependencyID = "3308";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e77fb521-941d-409f-8f67-d9ad9f00941c;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Update_login_form()";
							- _id = GUID 01e2fbdd-fd36-43b0-bb7a-23f29d518c55;
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID aceb84e0-74f1-4641-bdac-47d8cbd24bbd;
						- _name = "Show_actions_list";
						- _objectCreation = "81000711362017929142128";
						- _umlDependencyID = "3338";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e77fb521-941d-409f-8f67-d9ad9f00941c;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Show_actions_list()";
							- _id = GUID 7a042e9d-93c0-405c-bc85-46b37a578508;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID d2c722b7-24cc-46f8-8bef-332aed24a0b4;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 5ae17e4e-1258-47c6-8def-3c6d8d31a5d3;
						}
					}
					{ IMessage 
						- _id = GUID 51a923f4-a441-4a67-9cbd-624010c16afd;
						- _name = "Show_actions_list";
						- _objectCreation = "81000911362017929140128";
						- _umlDependencyID = "3338";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Show_actions_list()";
							- _id = GUID 8b6c286e-8dec-40cd-baca-4804117c3baf;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 7e7f13db-0ea7-4e1c-8409-ca11136c693d;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 212ce506-a180-4d0c-a76d-93eafd8436f0;
						}
					}
					{ IMessage 
						- _id = GUID d8d3664c-df5b-4833-bcbf-6e62729cd618;
						- _name = "Open_actions_list_form";
						- _objectCreation = "81001111362017929138128";
						- _umlDependencyID = "3854";
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Open_actions_list_form()";
							- _id = GUID f087fded-55a8-4fc0-9c17-539ff092a7e4;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 7ed9a8fc-4118-4f6a-baa8-60db72d99030;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 27a3608b-9825-4962-ad28-15f7bff80130;
						- _myState = 8192;
						- _name = "Choose_action";
						- _objectCreation = "81001311362017929136128";
						- _umlDependencyID = "2876";
						- m_szSequence = "7.";
						- m_szActualArgs = "\"mark_lesson\"";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Choose_action()";
							- _id = GUID ee3ec234-6c5d-43aa-b0fe-c35d90edd630;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 4666f6a6-20e4-476d-aa32-968b58bb2b85;
						- _name = "Update_action_form";
						- _objectCreation = "81001511362017929134128";
						- _umlDependencyID = "3409";
						- m_szSequence = "8.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Update_action_form()";
							- _id = GUID 1c7c63ae-03f2-4855-816a-9ad4a700ea78;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 078c692b-c4ad-47e9-ad73-40560c1ba2dc;
						- _name = "Synchronize_lessons_list";
						- _objectCreation = "81001711362017929132128";
						- _umlDependencyID = "4123";
						- m_szSequence = "9.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Synchronize_lessons_list()";
							- _id = GUID 0f0a2458-4039-42af-b828-d75724170546;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 0ebaa497-ea05-4001-b219-397b1950a512;
						- _myState = 8192;
						- _name = "Get_lesson";
						- _objectCreation = "81001911362017929130128";
						- _umlDependencyID = "2577";
						- m_szSequence = "10.";
						- m_szActualArgs = "Lesson";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_lesson()";
							- _id = GUID 60220377-c72c-4207-9866-11d415a922c1;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 662e301a-95fc-4ba9-86af-ecf6e96c55f3;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 9a86da0e-3802-4e24-aa0d-0bc2639a7174;
						}
					}
					{ IMessage 
						- _id = GUID b0940618-1f47-48db-b124-0bf8afad9f5d;
						- _myState = 8192;
						- _name = "Get_lesson";
						- _objectCreation = "81002111362017929128128";
						- _umlDependencyID = "2577";
						- m_szSequence = "11.";
						- m_szActualArgs = "Lesson";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 30229201-2f7e-4bab-ac3d-46b768e4bf51;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Lesson";
							- _name = "Get_lesson()";
							- _id = GUID cda49f6c-19dc-4023-9c2d-6916d171be6e;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 568a0bed-aa00-4b9f-9703-9cf47d0e24ce;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 0d38cfdf-9aab-4d7c-b7b3-10f83670f51c;
						}
					}
					{ IMessage 
						- _id = GUID 605d9c34-621f-4a88-a69d-455a4c3ab246;
						- _name = "Open_lessons_list_form";
						- _objectCreation = "81002311362017929126128";
						- _umlDependencyID = "3876";
						- m_szSequence = "12.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c113db99-b009-4f32-901a-d5408ab46910;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Open_lessons_list_form()";
							- _id = GUID 63adfea9-1083-49a1-8894-820c3c69f0bd;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID ad1ec94a-25ef-4915-a31f-42db8c31c019;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 59540170-899d-40af-848d-712fd225b197;
						}
					}
					{ IMessage 
						- _id = GUID 67947061-feae-482f-aef7-f497aa0a11cd;
						- _name = "Open_lessons_list_form";
						- _objectCreation = "81002511362017929124128";
						- _umlDependencyID = "3876";
						- m_szSequence = "13.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Open_lessons_list_form()";
							- _id = GUID 63adfea9-1083-49a1-8894-820c3c69f0bd;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 75d9e189-05e8-4f1f-80b1-55581cdc8a36;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 963c6239-69f9-4dbb-aadf-d94c8379bb79;
						- _myState = 8192;
						- _name = "Choose_lesson";
						- _objectCreation = "81002711362017929122128";
						- _umlDependencyID = "2898";
						- m_szSequence = "14.";
						- m_szActualArgs = "Lesson";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Choose_lesson()";
							- _id = GUID e3690f9a-fbf9-48b1-8424-e931a1643876;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 891054c3-2805-4899-8dbd-23a2b48b382e;
						- _name = "Open_lesson_form";
						- _objectCreation = "81002911362017929120128";
						- _umlDependencyID = "3222";
						- m_szSequence = "15.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Open_lesson_form()";
							- _id = GUID f16bf928-f740-40dc-92ec-ead70bd2363c;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 14434c37-5cfe-4c09-a9e3-51c8b391d687;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 3fdcae61-6ab7-47b9-87c9-d1a95074782c;
						}
					}
					{ IMessage 
						- _id = GUID e3b84458-9107-4206-b873-1bc0209added;
						- _name = "Open_lesson_form";
						- _objectCreation = "81003111362017929118128";
						- _umlDependencyID = "3222";
						- m_szSequence = "16.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Open_lesson_form()";
							- _id = GUID f16bf928-f740-40dc-92ec-ead70bd2363c;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 41b3450e-f078-4e5f-9c31-444c4f1436c1;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID a30e5764-c08d-42b1-b268-9dd2f4eb2f38;
						- _name = "Set_lesson_info";
						- _objectCreation = "81003311362017929116128";
						- _umlDependencyID = "3112";
						- m_szSequence = "17.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Set_lesson_info()";
							- _id = GUID 4df1eba5-4a6a-4e4a-8147-85166a39c78f;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID ffae52ad-ab99-4ca7-9093-13ac206e0200;
						- _name = "Open_present_list_form";
						- _objectCreation = "81003511362017929114128";
						- _umlDependencyID = "3870";
						- m_szSequence = "18.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Open_present_list_form()";
							- _id = GUID cbe79ce3-0f04-4baa-bc44-55491893bf9b;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 1e8f4d1c-b739-486c-9d48-ac812efea75a;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 0f6dfd04-cb5f-41cc-8738-2a3b444d8722;
						}
					}
					{ IMessage 
						- _id = GUID 68e38887-aa8b-4a29-b0d1-4a737f0019e0;
						- _name = "Open_present_list_form";
						- _objectCreation = "81003711362017929112128";
						- _umlDependencyID = "3870";
						- m_szSequence = "19.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Open_present_list_form()";
							- _id = GUID cbe79ce3-0f04-4baa-bc44-55491893bf9b;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 06152e2e-256b-4842-a336-d3c68714f3e8;
						- _name = "Synchronize_students_list";
						- _objectCreation = "81003911362017929110128";
						- _umlDependencyID = "4238";
						- m_szSequence = "20.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Synchronize_students_list()";
							- _id = GUID da68603f-7b4f-4069-922a-4874692863ec;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 5dc1048b-51e6-47ca-ab35-4fcdcbcb4240;
						- _myState = 8192;
						- _name = "Get_student";
						- _objectCreation = "81004111362017929108128";
						- _umlDependencyID = "2692";
						- m_szSequence = "21.";
						- m_szActualArgs = "Student";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_student()";
							- _id = GUID 18dfce0c-9c56-4b9d-81e3-bc2b9ba57713;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID e3be40ce-1cab-4555-8b36-aa2af87e6b80;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 72fe4751-7481-41ff-82f1-5aa16006caa7;
						}
					}
					{ IMessage 
						- _id = GUID fe91bbfe-d9c3-4d0e-844a-3ce7f6c999bd;
						- _myState = 8192;
						- _name = "Get_student";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204{\\*\\fname Arial;}Arial CYR;}}
\\viewkind4\\uc1\\pard\\f0\\fs20\\'c2\\'fb\\'e2\\'e5\\'f1\\'f2\\'e8 \\'f1\\'f2\\'f3\\'e4\\'e5\\'ed\\'f2\\'e0\\par
}
";
						- _objectCreation = "81004311362017929106128";
						- _umlDependencyID = "2692";
						- m_szSequence = "22.";
						- m_szActualArgs = "Student";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 8818da5d-b300-467c-a9bc-4387fb6b290d;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Server.sbs";
							- _subsystem = "Server";
							- _class = "Student";
							- _name = "Get_student()";
							- _id = GUID 11bb3ed6-a197-4577-a5ef-b55c164240f2;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 20f7de05-4c14-4945-977b-b98a83cedbb3;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID f526f247-c883-4382-92aa-4987e801da5a;
						}
					}
					{ IMessage 
						- _id = GUID cf85f063-c8b3-4ce2-af50-9be1b5981cf1;
						- _name = "Mark_present";
						- _objectCreation = "81004511362017929104128";
						- _umlDependencyID = "2793";
						- m_szSequence = "23.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Mark_present()";
							- _id = GUID d190ce5a-60c0-4f6f-9139-a9be45259497;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID f0b19860-f4b9-442f-b4ef-cf9132a19080;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 32387afc-7418-4333-8eea-130014ab7cfa;
						}
					}
					{ IMessage 
						- _id = GUID a3c624f8-c4a1-4765-a76d-ef48df7de367;
						- _myState = 8192;
						- _name = "Add_lesson_info";
						- _objectCreation = "81004711362017929102128";
						- _umlDependencyID = "3077";
						- m_szSequence = "24.";
						- m_szActualArgs = "Info";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Add_lesson_info()";
							- _id = GUID 9ac86a6c-f60a-4218-b053-844cbc2bf697;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 640e4a8a-aec4-4c62-8219-3ff6d7f817db;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 88674537-2f18-4283-98a3-37c41e00a0ca;
						}
					}
					{ IMessage 
						- _id = GUID 8959a2d9-14d8-45b6-924c-717c244141db;
						- _myState = 8192;
						- _name = "Update_lessons_list_form";
						- _objectCreation = "81004911362017929100128";
						- _umlDependencyID = "4085";
						- m_szSequence = "27.";
						- m_szActualArgs = "Info";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 493df700-cf2f-4786-b35f-0773baa4fcbd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonsListForm";
							- _name = "Update_lessons_list_form()";
							- _id = GUID 8b4ad549-8dc3-45b6-8c34-ab3cc7e8a37f;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 257abefd-7106-414b-a269-7d4de99051b8;
						- _name = "Close_lesson_info_form";
						- _objectCreation = "81005111362017929098128";
						- _umlDependencyID = "3854";
						- m_szSequence = "25.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 58d47199-ce4a-4cf4-9750-5e55d0f60a05;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Close_lesson_info_form()";
							- _id = GUID 95579811-cfea-471b-97d3-9ab134bdc3ed;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 43fed37a-3342-4088-8187-17175c081413;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 2fce1d53-b4b9-4cae-90c3-7a90a66325ef;
						}
					}
					{ IMessage 
						- _id = GUID dcd6eb35-cfb9-41da-8f5c-843027755416;
						- _name = "Close_present_list_form";
						- _objectCreation = "81005311362017929096128";
						- _umlDependencyID = "3979";
						- m_szSequence = "26.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1c7c59da-4a74-44ad-a4e7-6a22f73d05da;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ea891ea5-0705-4c7a-b578-25a8f1e60ba1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Close_present_list_form()";
							- _id = GUID d72d07f7-c6d8-4020-9477-9f656e92a7c8;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID dd6abadc-5d7b-46e4-a6fc-750f1671f4c2;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 24f71c12-a1e3-46ca-88e7-a285681dfe7b;
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 33;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 53184907-3e44-4f48-a59b-22043416bfc5;
						- _objectCreation = "81005511362017929094128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 1162968a-36fc-4c53-b888-49f3c2388ad9;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 6455d908-220c-416a-9a4a-693a628e41e2;
						- _objectCreation = "81005711362017929092128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 1162968a-36fc-4c53-b888-49f3c2388ad9;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID c32c491c-8b01-4292-a782-155820d14d8c;
						- _objectCreation = "81005911362017929090128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 9f4e4e93-519b-4f26-a933-64b77b4a1146;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 31e0967b-f1a2-4f1e-a001-b6a32374a2fe;
						- _objectCreation = "81006111362017929088128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 9f4e4e93-519b-4f26-a933-64b77b4a1146;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 127;
					}
					{ IExecutionOccurrence 
						- _id = GUID d2c722b7-24cc-46f8-8bef-332aed24a0b4;
						- _objectCreation = "81006311362017929086128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID aceb84e0-74f1-4641-bdac-47d8cbd24bbd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 65;
					}
					{ IExecutionOccurrence 
						- _id = GUID 5ae17e4e-1258-47c6-8def-3c6d8d31a5d3;
						- _objectCreation = "81006511362017929084128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID aceb84e0-74f1-4641-bdac-47d8cbd24bbd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 7e7f13db-0ea7-4e1c-8409-ca11136c693d;
						- _objectCreation = "81006711362017929082128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 51a923f4-a441-4a67-9cbd-624010c16afd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 45;
					}
					{ IExecutionOccurrence 
						- _id = GUID 212ce506-a180-4d0c-a76d-93eafd8436f0;
						- _objectCreation = "81006911362017929080128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 51a923f4-a441-4a67-9cbd-624010c16afd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 85;
					}
					{ IExecutionOccurrence 
						- _id = GUID 7ed9a8fc-4118-4f6a-baa8-60db72d99030;
						- _objectCreation = "81007111362017929078128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d8d3664c-df5b-4833-bcbf-6e62729cd618;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 217;
					}
					{ IExecutionOccurrence 
						- _id = GUID 662e301a-95fc-4ba9-86af-ecf6e96c55f3;
						- _objectCreation = "81007311362017929076128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 0ebaa497-ea05-4001-b219-397b1950a512;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 91;
					}
					{ IExecutionOccurrence 
						- _id = GUID 9a86da0e-3802-4e24-aa0d-0bc2639a7174;
						- _objectCreation = "81007511362017929074128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 0ebaa497-ea05-4001-b219-397b1950a512;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 568a0bed-aa00-4b9f-9703-9cf47d0e24ce;
						- _objectCreation = "81007711362017929072128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID b0940618-1f47-48db-b124-0bf8afad9f5d;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 102;
					}
					{ IExecutionOccurrence 
						- _id = GUID 0d38cfdf-9aab-4d7c-b7b3-10f83670f51c;
						- _objectCreation = "81007911362017929070128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID b0940618-1f47-48db-b124-0bf8afad9f5d;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID ad1ec94a-25ef-4915-a31f-42db8c31c019;
						- _objectCreation = "81008111362017929068128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 605d9c34-621f-4a88-a69d-455a4c3ab246;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 41;
					}
					{ IExecutionOccurrence 
						- _id = GUID 59540170-899d-40af-848d-712fd225b197;
						- _objectCreation = "81008311362017929066128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 605d9c34-621f-4a88-a69d-455a4c3ab246;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 97;
					}
					{ IExecutionOccurrence 
						- _id = GUID 75d9e189-05e8-4f1f-80b1-55581cdc8a36;
						- _objectCreation = "81008511362017929064128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 67947061-feae-482f-aef7-f497aa0a11cd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 161;
					}
					{ IExecutionOccurrence 
						- _id = GUID 14434c37-5cfe-4c09-a9e3-51c8b391d687;
						- _objectCreation = "81008711362017929062128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 891054c3-2805-4899-8dbd-23a2b48b382e;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 43;
					}
					{ IExecutionOccurrence 
						- _id = GUID 3fdcae61-6ab7-47b9-87c9-d1a95074782c;
						- _objectCreation = "81008911362017929060128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 891054c3-2805-4899-8dbd-23a2b48b382e;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 41b3450e-f078-4e5f-9c31-444c4f1436c1;
						- _objectCreation = "81009111362017929058128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID e3b84458-9107-4206-b873-1bc0209added;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 127;
					}
					{ IExecutionOccurrence 
						- _id = GUID 1e8f4d1c-b739-486c-9d48-ac812efea75a;
						- _objectCreation = "81009311362017929056128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID ffae52ad-ab99-4ca7-9093-13ac206e0200;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 214;
					}
					{ IExecutionOccurrence 
						- _id = GUID 0f6dfd04-cb5f-41cc-8738-2a3b444d8722;
						- _objectCreation = "81009511362017929054128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID ffae52ad-ab99-4ca7-9093-13ac206e0200;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID e3be40ce-1cab-4555-8b36-aa2af87e6b80;
						- _objectCreation = "81009711362017929052128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 5dc1048b-51e6-47ca-ab35-4fcdcbcb4240;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 85;
					}
					{ IExecutionOccurrence 
						- _id = GUID 72fe4751-7481-41ff-82f1-5aa16006caa7;
						- _objectCreation = "81009911362017929050128";
						- _umlDependencyID = "1543";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 5dc1048b-51e6-47ca-ab35-4fcdcbcb4240;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 20f7de05-4c14-4945-977b-b98a83cedbb3;
						- _objectCreation = "81010111362017929048128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID fe91bbfe-d9c3-4d0e-844a-3ce7f6c999bd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID f526f247-c883-4382-92aa-4987e801da5a;
						- _objectCreation = "81010311362017929046128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID fe91bbfe-d9c3-4d0e-844a-3ce7f6c999bd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID f0b19860-f4b9-442f-b4ef-cf9132a19080;
						- _objectCreation = "81010511362017929044128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID cf85f063-c8b3-4ce2-af50-9be1b5981cf1;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 67;
					}
					{ IExecutionOccurrence 
						- _id = GUID 32387afc-7418-4333-8eea-130014ab7cfa;
						- _objectCreation = "81010711362017929042128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID cf85f063-c8b3-4ce2-af50-9be1b5981cf1;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 640e4a8a-aec4-4c62-8219-3ff6d7f817db;
						- _objectCreation = "81010911362017929040128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a3c624f8-c4a1-4765-a76d-ef48df7de367;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 135;
					}
					{ IExecutionOccurrence 
						- _id = GUID 88674537-2f18-4283-98a3-37c41e00a0ca;
						- _objectCreation = "81011111362017929038128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a3c624f8-c4a1-4765-a76d-ef48df7de367;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 43fed37a-3342-4088-8187-17175c081413;
						- _objectCreation = "81011311362017929036128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 257abefd-7106-414b-a269-7d4de99051b8;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 68;
					}
					{ IExecutionOccurrence 
						- _id = GUID 2fce1d53-b4b9-4cae-90c3-7a90a66325ef;
						- _objectCreation = "81011511362017929034128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 257abefd-7106-414b-a269-7d4de99051b8;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID dd6abadc-5d7b-46e4-a6fc-750f1671f4c2;
						- _objectCreation = "81011711362017929032128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID dcd6eb35-cfb9-41da-8f5c-843027755416;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 24f71c12-a1e3-46ca-88e7-a285681dfe7b;
						- _objectCreation = "81011911362017929030128";
						- _umlDependencyID = "1534";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID dcd6eb35-cfb9-41da-8f5c-843027755416;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
				}
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID 0682decb-6a11-4def-b0c2-45b22d2fd8fb;
		}
	}
	- UCDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IUCDiagram 
			- _id = GUID 0b21888a-f847-4c4a-b212-3b092a71d3d6;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Actor";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,26,84,168";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "UseCase";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,21,129,92";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "grid_snap";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "main";
			- _objectCreation = "81012111362017929028128";
			- _umlDependencyID = "1955";
			- _lastModifiedTime = "12.11.2017::2:36:0";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 04320f93-3a9e-4c4d-bf3e-ada371b0fd35;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IUCDiagram";
					- _id = GUID 0b21888a-f847-4c4a-b212-3b092a71d3d6;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 35;
				{ CGIClass 
					- _id = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID bc801e60-7039-4358-9271-a50ac2b9ba9b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIBasicClass 
					- _id = GUID ae86f893-2bd9-4b42-82e1-729c69421ebb;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "\À\á\è\ò\ó\ð\è\å\í\ò";
						- _id = GUID 6c37dd20-4808-4dd0-beb9-abaf20f8a720;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "\À\á\è\ò\ó\ð\è\å\í\ò";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 3.89464 -30.9773 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 1a4b507b-f032-4a0e-82ad-646c9fec6280;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "\Ê\ë\è\å\í\ò-\ì\å\í\å\ä\æ\å\ð";
						- _id = GUID 68883e54-994b-4611-9481-719ae9e226ae;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "\Ê\ë\è\å\í\ò-\ì\å\í\å\ä\æ\å\ð";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 396.895 -30.9773 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID b8cd83cc-cee8-47c8-b69e-f3d9f34a29e3;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "\Ï\ð\î\ã\ð\à\ì\ì\í\û\é \ì\å\í\å\ä\æ\å\ð";
						- _id = GUID bfc2e385-998e-4bc2-a5c9-9459fe75308a;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "\Ï\ð\î\ã\ð\à\ì\ì\í\û\é \ì\å\í\å\ä\æ\å\ð";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 806.895 -30.9773 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 5e4f982b-cd47-4508-9aea-3b1035aa3d83;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "\Ä\è\ñ\ï\å\ò\÷\å\ð";
						- _id = GUID 7f8b542f-0b47-49ca-9390-0e08d04c2fe7;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "\Ä\è\ñ\ï\å\ò\÷\å\ð";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 -0.105347 189.023 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 9c1cfde2-71ba-4e8c-9e5a-3678475e2c27;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _id = GUID 897bea32-c27a-43fe-b2e4-fdd78255e3b9;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 401.895 175.023 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 47060dab-eeac-40f5-93d1-84c74796ed5c;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "\Ñ\ò\ó\ä\å\í\ò";
						- _id = GUID 68de63f1-49cb-4752-8c01-6d71a665c56f;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "\Ñ\ò\ó\ä\å\í\ò";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 -3.10535 409.023 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 02356a54-2f29-4fc1-94c6-0d57c9844367;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "\Ä\å\ê\à\í\à\ò";
						- _id = GUID 39336f2b-c764-4e4c-a704-a05a36ba9f0c;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "\Ä\å\ê\à\í\à\ò";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 807.895 161.023 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 303a15ba-5a1e-4558-903d-c723793b7dff;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "1. \Ï\ð\î\ñ\ì\î\ò\ð\ò\ü \ñ\ï\è\ñ\î\ê \í\à\ï\ð\à\â\ë\å\í\è\é";
						- _id = GUID 28265bcf-8ef5-4a56-910e-127ee36b7f4b;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "1. \Ï\ð\î\ñ\ì\î\ò\ð\ò\ü \ñ\ï\è\ñ\î\ê \í\à\ï\ð\à\â\ë\å\í\è\é";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.194863 0 0 0.0662932 124.39 0.0662918 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 1d35e072-e9aa-4061-be78-e78b4313a7ed;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "2. \Ï\î\ä\à\ò\ü \ç\à\ÿ\â\ê\ó \í\à \ç\à\ï\è\ñ\ü \â \ã\ð\ó\ï\ï\ó";
						- _id = GUID 973dd4d8-a805-4017-9787-4c287a66746c;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "2. \Ï\î\ä\à\ò\ü \ç\à\ÿ\â\ê\ó \í\à \ç\à\ï\è\ñ\ü \â \ã\ð\ó\ï\ï\ó";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.194863 0 0 0.0662932 124.39 96.0663 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID c3ab14bc-5751-4422-98da-186b79dd28de;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\À\á\è\ò\ó\ð\è\å\í\ò";
						- _name = "its1. \Ï\ð\î\ñ\ì\î\ò\ð\ò\ü \ñ\ï\è\ñ\î\ê \í\à\ï\ð\à\â\ë\å\í\è\é";
						- _id = GUID 46b2504a-a097-457f-aeb6-39a46f214f2d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ae86f893-2bd9-4b42-82e1-729c69421ebb;
					- m_sourceType = 'F';
					- m_pTarget = GUID 303a15ba-5a1e-4558-903d-c723793b7dff;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 658 807 ;
					- m_TargetPort = 100 497 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "1. \Ï\ð\î\ñ\ì\î\ò\ð\ò\ü \ñ\ï\è\ñ\î\ê \í\à\ï\ð\à\â\ë\å\í\è\é";
						- _name = "its\À\á\è\ò\ó\ð\è\å\í\ò";
						- _id = GUID 8118dd6d-f20d-4b98-86e4-9c9ac9941b02;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID bc836703-fc88-42d7-87ec-097540ce336a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\À\á\è\ò\ó\ð\è\å\í\ò";
						- _name = "its2. \Ï\î\ä\à\ò\ü \ç\à\ÿ\â\ê\ó \í\à \ç\à\ï\è\ñ\ü \â \ã\ð\ó\ï\ï\ó";
						- _id = GUID a47e34da-801f-47d3-9a56-e38d1ce0a976;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ae86f893-2bd9-4b42-82e1-729c69421ebb;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1d35e072-e9aa-4061-be78-e78b4313a7ed;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 658 807 ;
					- m_TargetPort = 333 406 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "2. \Ï\î\ä\à\ò\ü \ç\à\ÿ\â\ê\ó \í\à \ç\à\ï\è\ñ\ü \â \ã\ð\ó\ï\ï\ó";
						- _name = "its\À\á\è\ò\ó\ð\è\å\í\ò";
						- _id = GUID bb69e0b0-fe4b-4a17-b166-d33f58b90e7b;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIBasicClass 
					- _id = GUID 052bf9a3-efc7-4391-9878-f38074a0d0b1;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "3. \Ç\à\ï\è\ñ\à\ò\ü \à\á\è\ò\ó\ð\è\å\í\ò\à \â \ã\ð\ó\ï\ï\ó";
						- _id = GUID bf935208-9f78-470b-b1e4-7f54aac46360;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "3. \Ç\à\ï\è\ñ\à\ò\ü \à\á\è\ò\ó\ð\è\å\í\ò\à \â \ã\ð\ó\ï\ï\ó";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.182462 0 0 0.0662932 536.365 28.0663 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID 74c03f16-fbe4-4c2f-9975-7834b2638948;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ê\ë\è\å\í\ò-\ì\å\í\å\ä\æ\å\ð";
						- _name = "its3. \Ç\à\ï\è\ñ\à\ò\ü \à\á\è\ò\ó\ð\è\å\í\ò\à \â \ã\ð\ó\ï\ï\ó";
						- _id = GUID 423ef6dc-39bd-49a5-82e5-a7aca140292e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1a4b507b-f032-4a0e-82ad-646c9fec6280;
					- m_sourceType = 'F';
					- m_pTarget = GUID 052bf9a3-efc7-4391-9878-f38074a0d0b1;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 555 807 ;
					- m_TargetPort = 140 542 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "3. \Ç\à\ï\è\ñ\à\ò\ü \à\á\è\ò\ó\ð\è\å\í\ò\à \â \ã\ð\ó\ï\ï\ó";
						- _name = "its\Ê\ë\è\å\í\ò-\ì\å\í\å\ä\æ\å\ð";
						- _id = GUID c0e693b3-9a23-49ac-903e-752c5d1892a3;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIBasicClass 
					- _id = GUID 582d330c-f89f-40f6-9447-fb7282274268;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "4. \Ñ\î\ñ\ò\à\â\è\ò\ü \ó\÷\å\á\í\û\é \ï\ë\à\í";
						- _id = GUID 0a80ebf0-cc7a-41ea-87fe-01c45d2a07e7;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "4. \Ñ\î\ñ\ò\à\â\è\ò\ü \ó\÷\å\á\í\û\é \ï\ë\à\í";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.194863 0 0 0.0662932 963.39 41.0663 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID 0df63c64-3188-4537-a52f-9873b56b3baa;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ï\ð\î\ã\ð\à\ì\ì\í\û\é \ì\å\í\å\ä\æ\å\ð";
						- _name = "its4. \Ñ\î\ñ\ò\à\â\è\ò\ü \ó\÷\å\á\í\û\é \ï\ë\à\í";
						- _id = GUID 194eeae0-b77a-44e7-ab5a-04f8b69d71e8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b8cd83cc-cee8-47c8-b69e-f3d9f34a29e3;
					- m_sourceType = 'F';
					- m_pTarget = GUID 582d330c-f89f-40f6-9447-fb7282274268;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 594 694 ;
					- m_TargetPort = 182 421 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "4. \Ñ\î\ñ\ò\à\â\è\ò\ü \ó\÷\å\á\í\û\é \ï\ë\à\í";
						- _name = "its\Ï\ð\î\ã\ð\à\ì\ì\í\û\é \ì\å\í\å\ä\æ\å\ð";
						- _id = GUID 8d31e126-2642-431f-a20f-98a3a494f19f;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIBasicClass 
					- _id = GUID 53714cb0-c21b-4bf2-9583-af49d6243cd0;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "5. \Ñ\ô\î\ð\ì\è\ð\î\â\à\ò\ü \ð\à\ñ\ï\è\ñ\à\í\è\å";
						- _id = GUID 46791354-1911-4d2e-8943-a6f09de83396;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "5. \Ñ\ô\î\ð\ì\è\ð\î\â\à\ò\ü \ð\à\ñ\ï\è\ñ\à\í\è\å";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.194863 0 0 0.0662932 124.39 220.066 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID a69cd64f-0eab-420e-90ae-d2d19d2aad76;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "6. \Ï\ð\î\à\í\à\ë\è\ç\è\ð\î\â\à\ò\ü \ï\î\ë\í\î\ò\ó \â\û\ï\î\ë\í\å\í\è\ÿ \ó\÷\å\á\í\î\é \í\à\ã\ð\ó\ç\ê\è";
						- _id = GUID 18d95ccb-320c-4af7-95dd-8086180d5187;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "6. \Ï\ð\î\à\í\à\ë\è\ç\è\ð\î\â\à\ò\ü \ï\î\ë\í\î\ò\ó \â\û\ï\î\ë\í\å\í\è\ÿ \ó\÷\å\á\í\î\é \í\à\ã\ð\ó\ç\ê\è";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.194863 0 0 0.0774977 124.39 302.077 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID cec9bd35-4c9f-47f0-8e02-d8c7e6edb635;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ä\è\ñ\ï\å\ò\÷\å\ð";
						- _name = "its5. \Ñ\ô\î\ð\ì\è\ð\î\â\à\ò\ü \ð\à\ñ\ï\è\ñ\à\í\è\å";
						- _id = GUID 035938ae-908a-4edb-a047-152641d238da;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 5e4f982b-cd47-4508-9aea-3b1035aa3d83;
					- m_sourceType = 'F';
					- m_pTarget = GUID 53714cb0-c21b-4bf2-9583-af49d6243cd0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 529 694 ;
					- m_TargetPort = 279 406 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "5. \Ñ\ô\î\ð\ì\è\ð\î\â\à\ò\ü \ð\à\ñ\ï\è\ñ\à\í\è\å";
						- _name = "its\Ä\è\ñ\ï\å\ò\÷\å\ð";
						- _id = GUID ca3be703-3088-45c3-9db9-8c329769f39b;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID b9ae7077-c733-4a9d-8214-f270be50e656;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ä\è\ñ\ï\å\ò\÷\å\ð";
						- _name = "its6. \Ï\ð\î\à\í\à\ë\è\ç\è\ð\î\â\à\ò\ü \ï\î\ë\í\î\ò\ó \â\û\ï\î\ë\í\å\í\è\ÿ \ó\÷\å\á\í\î\é \í\à\ã\ð\ó\ç\ê\è";
						- _id = GUID dac290e5-4bf1-4438-aa48-fc88781d7a10;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 5e4f982b-cd47-4508-9aea-3b1035aa3d83;
					- m_sourceType = 'F';
					- m_pTarget = GUID a69cd64f-0eab-420e-90ae-d2d19d2aad76;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 529 807 ;
					- m_TargetPort = 306 557 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "6. \Ï\ð\î\à\í\à\ë\è\ç\è\ð\î\â\à\ò\ü \ï\î\ë\í\î\ò\ó \â\û\ï\î\ë\í\å\í\è\ÿ \ó\÷\å\á\í\î\é \í\à\ã\ð\ó\ç\ê\è";
						- _name = "its\Ä\è\ñ\ï\å\ò\÷\å\ð";
						- _id = GUID 9d0aa38a-7693-4dbc-bbf4-c0a35d7093da;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIBasicClass 
					- _id = GUID ca6d00e6-d0f9-4c76-9f8d-de367630dde6;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "7. \Î\ò\ì\å\ò\è\ò\ü \ï\ð\î\â\å\ä\å\í\í\î\å \ç\à\í\ÿ\ò\è\å";
						- _id = GUID 88d46171-667c-481e-b667-d4ffc60bdeb1;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "7. \Î\ò\ì\å\ò\è\ò\ü \ï\ð\î\â\å\ä\å\í\í\î\å \ç\à\í\ÿ\ò\è\å";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.183348 0 0 0.0662932 536.367 165.066 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID dbfe6106-c104-43f5-84d1-0bfbac67812d;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "8. \Ï\î\ñ\ò\à\â\è\ò\ü \î\ö\å\í\ê\ó \ñ\ò\ó\ä\å\í\ò\ó";
						- _id = GUID 238aaa3b-d82a-4f46-ac3d-d32150e2d229;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "8. \Ï\î\ñ\ò\à\â\è\ò\ü \î\ö\å\í\ê\ó \ñ\ò\ó\ä\å\í\ò\ó";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.183348 0 0 0.0662932 536.367 330.066 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 448c3019-f452-4893-9efe-1d8d3daeda9c;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "9. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \ò\å\ê\ó\ù\å\å \ð\à\ñ\ï\è\ñ\à\í\è\å \ç\à\í\ÿ\ò\è\é";
						- _id = GUID a82e7724-d23c-4d74-8101-e5a91bb4c226;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "9. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \ò\å\ê\ó\ù\å\å \ð\à\ñ\ï\è\ñ\à\í\è\å \ç\à\í\ÿ\ò\è\é";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.194863 0 0 0.0793651 124.39 399.079 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID c6b80ee3-6abb-4177-b21a-8a892dcbc631;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "10. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\ö\å\í\ê\è \ñ\ò\ó\ä\å\í\ò\à";
						- _id = GUID dcf1194a-270f-4e68-a4d3-a41b4f40a74f;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "10. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\ö\å\í\ê\è \ñ\ò\ó\ä\å\í\ò\à";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.158547 0 0 0.0662932 124.317 495.066 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 8b352b98-c00a-43f7-9bf0-b1b86478607f;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "11. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\ÿ \ä\å\ê\à\í\à\ò\à";
						- _id = GUID 05006ebc-1d70-46b4-89e3-b1d37f0903dd;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "11. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\ÿ \ä\å\ê\à\í\à\ò\à";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.182462 0 0 0.0662932 124.365 578.066 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID e3048611-fe18-4b35-8d75-2335fae8a543;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "12. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \è\í\ô\î\ð\ì\à\ö\è\þ \î \ñ\ò\ó\ä\å\í\ò\å";
						- _id = GUID 285fb111-bcd9-42d0-bb8e-4b6183f97b68;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "12. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \è\í\ô\î\ð\ì\à\ö\è\þ \î \ñ\ò\ó\ä\å\í\ò\å";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.218778 0 0 0.0662932 963.438 192.066 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 64ecbf0e-26fc-465f-b7ca-8da194400dff;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "13. \Ñ\ä\å\ë\à\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\å";
						- _id = GUID 8727b9d7-fc66-4fab-a414-eaa011b05fa2;
					}
					- m_pParent = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
					- m_name = { CGIText 
						- m_str = "13. \Ñ\ä\å\ë\à\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\å";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.194863 0 0 0.0662932 963.39 275.066 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID 7cb53c1f-7ba6-44a5-b8e7-9fc259a258de;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ä\å\ê\à\í\à\ò";
						- _name = "its12. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \è\í\ô\î\ð\ì\à\ö\è\þ \î \ñ\ò\ó\ä\å\í\ò\å";
						- _id = GUID a4a3a730-67d5-43a2-ab6e-e97aa935fcc6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 02356a54-2f29-4fc1-94c6-0d57c9844367;
					- m_sourceType = 'F';
					- m_pTarget = GUID e3048611-fe18-4b35-8d75-2335fae8a543;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 581 694 ;
					- m_TargetPort = 169 587 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "12. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \è\í\ô\î\ð\ì\à\ö\è\þ \î \ñ\ò\ó\ä\å\í\ò\å";
						- _name = "its\Ä\å\ê\à\í\à\ò";
						- _id = GUID 289fc834-a04f-43c2-be48-e77a2ede7827;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 9fb5ae17-dd6e-4b2b-87a1-62ab3cb3fad1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ä\å\ê\à\í\à\ò";
						- _name = "its13. \Ñ\ä\å\ë\à\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\å";
						- _id = GUID a227fb28-97e3-4d5e-9a11-d540df4d1a0f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 02356a54-2f29-4fc1-94c6-0d57c9844367;
					- m_sourceType = 'F';
					- m_pTarget = GUID 64ecbf0e-26fc-465f-b7ca-8da194400dff;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 581 807 ;
					- m_TargetPort = 383 436 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "13. \Ñ\ä\å\ë\à\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\å";
						- _name = "its\Ä\å\ê\à\í\à\ò";
						- _id = GUID 28b26c90-a370-4937-9588-bc6b54cc14eb;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 82a3a166-ae59-44bb-bf82-da25534a3d08;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _name = "its7. \Î\ò\ì\å\ò\è\ò\ü \ï\ð\î\â\å\ä\å\í\í\î\å \ç\à\í\ÿ\ò\è\å";
						- _id = GUID cc2e7273-d1d7-42a9-8bd3-3562e5153f35;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9c1cfde2-71ba-4e8c-9e5a-3678475e2c27;
					- m_sourceType = 'F';
					- m_pTarget = GUID ca6d00e6-d0f9-4c76-9f8d-de367630dde6;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 491 694 ;
					- m_TargetPort = 415 542 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "7. \Î\ò\ì\å\ò\è\ò\ü \ï\ð\î\â\å\ä\å\í\í\î\å \ç\à\í\ÿ\ò\è\å";
						- _name = "its\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _id = GUID 69683185-fb9f-4a84-957c-a187f6344115;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 3b09477f-108f-403c-b5f2-24de89d2ee2c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _name = "its8. \Ï\î\ñ\ò\à\â\è\ò\ü \î\ö\å\í\ê\ó \ñ\ò\ó\ä\å\í\ò\ó";
						- _id = GUID baedab1c-567e-4363-a887-72b7114eeeab;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9c1cfde2-71ba-4e8c-9e5a-3678475e2c27;
					- m_sourceType = 'F';
					- m_pTarget = GUID dbfe6106-c104-43f5-84d1-0bfbac67812d;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 671 807 ;
					- m_TargetPort = 325 482 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "8. \Ï\î\ñ\ò\à\â\è\ò\ü \î\ö\å\í\ê\ó \ñ\ò\ó\ä\å\í\ò\ó";
						- _name = "its\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _id = GUID 247c1ba4-23e7-4b40-8d58-89cbb0f8a47e;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 12380d90-1915-4e9f-80c2-254d36601054;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ñ\ò\ó\ä\å\í\ò";
						- _name = "its9. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \ò\å\ê\ó\ù\å\å \ð\à\ñ\ï\è\ñ\à\í\è\å \ç\à\í\ÿ\ò\è\é";
						- _id = GUID fd59d288-ec2c-46f0-872e-253a8f9bbc7f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 47060dab-eeac-40f5-93d1-84c74796ed5c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 448c3019-f452-4893-9efe-1d8d3daeda9c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 568 702 ;
					- m_TargetPort = 261 512 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "9. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \ò\å\ê\ó\ù\å\å \ð\à\ñ\ï\è\ñ\à\í\è\å \ç\à\í\ÿ\ò\è\é";
						- _name = "its\Ñ\ò\ó\ä\å\í\ò";
						- _id = GUID cbcf0280-bf2d-41ec-bb48-3d6bb28bf393;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID d0654327-2362-4e92-a873-2449f20942bd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ñ\ò\ó\ä\å\í\ò";
						- _name = "its10. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\ö\å\í\ê\è \ñ\ò\ó\ä\å\í\ò\à";
						- _id = GUID 656afc01-bfea-41d3-8327-8fb3312523f9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 47060dab-eeac-40f5-93d1-84c74796ed5c;
					- m_sourceType = 'F';
					- m_pTarget = GUID c6b80ee3-6abb-4177-b21a-8a892dcbc631;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 568 807 ;
					- m_TargetPort = 292 436 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "10. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\ö\å\í\ê\è \ñ\ò\ó\ä\å\í\ò\à";
						- _name = "its\Ñ\ò\ó\ä\å\í\ò";
						- _id = GUID ee518bd7-2b0f-448f-b1c4-694764925125;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID aa40045e-b291-45ad-a214-a276c07a026d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ñ\ò\ó\ä\å\í\ò";
						- _name = "its11. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\ÿ \ä\å\ê\à\í\à\ò\à";
						- _id = GUID b0c5be7b-f3a4-4603-af45-72c4b23a98b3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 47060dab-eeac-40f5-93d1-84c74796ed5c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b352b98-c00a-43f7-9bf0-b1b86478607f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 568 807 ;
					- m_TargetPort = 566 814 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "11. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\ÿ \ä\å\ê\à\í\à\ò\à";
						- _name = "its\Ñ\ò\ó\ä\å\í\ò";
						- _id = GUID d0fd54c1-fe13-45f3-a718-60345345753d;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID fdf77893-0c49-48d4-b232-d3301f38f4a0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 94;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _name = "its11. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\ÿ \ä\å\ê\à\í\à\ò\à";
						- _id = GUID 4069e72a-d4d3-4952-b049-a6829b9102c8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9c1cfde2-71ba-4e8c-9e5a-3678475e2c27;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b352b98-c00a-43f7-9bf0-b1b86478607f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 607 807 ;
					- m_TargetPort = 925 286 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "11. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \î\á\ú\ÿ\â\ë\å\í\è\ÿ \ä\å\ê\à\í\à\ò\à";
						- _name = "its\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _id = GUID 6a1a55f6-9d42-4425-aaf3-85c77aa42d1f;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 0;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 0;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 0;
					- m_bShowQualifier2 = 0;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID ea1663c4-fc98-478a-9ffb-67271d0c58f3;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID cf4e5791-17f7-4f3a-aea9-10c877756e55;
			}
		}
	}
}

