I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID 23600686-f0fd-4ff5-8b64-6d46d9b6da4f;
	- _myState = 8192;
	- _name = "Studyhood";
	- _objectCreation = "320268116201721-3402123";
	- _umlDependencyID = "2476";
	- _lastID = 11;
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
			- _objectCreation = "320734116201721-3868123";
			- _umlDependencyID = "1916";
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
			- _objectCreation = "320736116201721-3870123";
			- _umlDependencyID = "1522";
			- _lastModifiedTime = "12.11.2017::13:49:8";
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
						- size = 11;
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
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Add_mark_info()";
							- _id = GUID 5f21b1c9-5000-46c7-a4fe-4e7370292cb8;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_groups_list()";
							- _id = GUID bdc9c9bf-fb6d-4d89-9aa7-be0268ec74f2;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Update_groups_list()";
							- _id = GUID 736d2655-5393-421f-a34c-9fa5cd3ecda7;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_schedule()";
							- _id = GUID 5bd0aed7-d93b-4082-bd10-038edde2ac06;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Update_schedule_form()";
							- _id = GUID e3b6d1bb-77c8-421b-bc89-8d188defb694;
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
						- size = 13;
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
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Synchronize_students_list()";
							- _id = GUID e2e14efe-effa-44be-b299-158c07a86d05;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Synchronize_groups_lists()";
							- _id = GUID 298cd612-88be-4476-bc9c-4b1e2f3b0b47;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Synchronize_groups_list()";
							- _id = GUID 96036464-df2e-47fe-b08e-56783b191ed2;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Choose_group()";
							- _id = GUID 448532c2-b3e1-4297-bfc7-45437abf649d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Open_schedule_form()";
							- _id = GUID 2c714dde-d3bf-4b53-9348-0301b92b58be;
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
							- _name = "Date_Edit";
							- _id = GUID 11038464-b67b-4b92-a26c-d4c2bedcbf7a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Time_Edit";
							- _id = GUID 46faeda4-820e-46c7-9c73-8c0ccd2ef362;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Subject_Edit";
							- _id = GUID a522eb39-dd1e-4a85-87b8-86556b672b11;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Groups_Edit";
							- _id = GUID 1ebb86d5-b8bb-48d3-ac09-34c9ae5fff1c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Room_Edit";
							- _id = GUID 85e12b84-622b-4033-80b3-3577702e4ea8;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LessonInfoForm";
							- _name = "Type_Edit";
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
						- size = 6;
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
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Mark_present()";
							- _id = GUID ea2cfc35-ae83-4db0-a18e-5fe76057427e;
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
		- size = 6;
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
							- size = 7;
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
								- _Name = "DestructionEvent";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,30,30";
										- _Type = String;
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
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "2";
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
			- _objectCreation = "320738116201721-3872123";
			- _umlDependencyID = "3069";
			- _lastModifiedTime = "12.11.2017::14:0:54";
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
				- elementList = 63;
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
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 1df0b941-f3b3-42b4-b0d4-1e8058496769;
					}
					- m_pParent = GUID fa72eda5-72ee-444f-9d0f-7ff3eead2068;
					- m_name = { CGIText 
						- m_str = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü:\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
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
					- m_transform = 1.38542 0 0 0.0327951 10 50 ;
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
					- m_transform = 2.04167 0 0 0.0327904 152 50 ;
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
					- m_transform = 2.48958 0 0 0.0327904 358 50 ;
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
					- m_transform = 2.26042 0 0 0.0327904 607 50 ;
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
					- m_transform = 2.33333 0 0 0.0327904 833 50 ;
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
					- m_transform = 0.895833 0 0 0.0327904 1067 50 ;
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
					- m_transform = 2.0625 0 0 0.0327904 1173 50 ;
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
					- m_transform = 2.26042 0 0 0.0327904 1381 50 ;
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
					- m_transform = 2.22917 0 0 0.0327904 1608 50 ;
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
					- m_transform = 0.721804 0 0 30.4923 43.4548 3323.67 ;
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
					- m_transform = 0.489796 0 0 30.4966 45.2373 3324.13 ;
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
					- m_transform = 0.489796 0 0 83.0185 45.2373 5336.91 ;
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
					- m_transform = 0.401674 0 0 30.4966 45.3876 5336.91 ;
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
					- m_transform = 0.401674 0 0 55.0633 45.3876 7227.7 ;
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
					- m_transform = 0.442396 0 0 38.1207 44.9054 8112.11 ;
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
					- m_transform = 0.442396 0 0 192.298 44.9054 10734.9 ;
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
					- m_transform = 0.401674 0 0 77.0885 45.3876 16559.6 ;
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
					- m_transform = 1.11628 0 0 30.4967 41.3803 18237 ;
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
					- m_transform = 0.442396 0 0 30.4966 44.9054 19944.8 ;
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
					- m_transform = 0.428573 0 0 34.7323 45.6009 19944.8 ;
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
					- m_transform = 0.428573 0 0 120.292 45.6009 22445.5 ;
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
					- m_transform = 0.484848 0 0 36.4265 45.079 25678.2 ;
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
					- m_transform = 0.484848 0 0 122.834 45.079 27569 ;
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
					- m_transform = 0.442396 0 0 166.884 45.102 30893.1 ;
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
					- m_transform = 0.401674 0 0 72.0059 45.3876 35802.9 ;
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
					- m_transform = 0.448598 0 0 30.4967 45.3458 37297.4 ;
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
					- m_transform = 0.484848 0 0 59.2991 45.079 40865.5 ;
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
					- m_transform = 0.401674 0 0 122.834 45.3876 41810.8 ;
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
					- m_transform = 0.484848 0 0 57.6048 45.079 43518.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID df9011b7-91cc-4ac2-ace9-a5cebd54a1c0;
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
					- m_transform = 0.442396 0 0 30.4967 45.102 44494.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b67c26fa-1361-4563-8198-4aa4b0d80b0a;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 9ccf7fdc-2284-4999-863c-fefa1fce0272;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 746142de-b021-40b1-92bd-6f425d6c75b2;
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
					- m_transform = 0.721803 0 0 30.4924 43.4547 11770 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID c7917d82-1e3c-41b0-b715-6c08dab70831;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID e245815a-2389-46c6-9f3c-975db95b5231;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 7c4daa2a-3029-40ad-b1e3-9d734d1f9c4e;
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
					- m_transform = 0.721803 0 0 30.4924 43.4547 29181.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID d8b5e709-1ccf-44c5-91ff-dda44f18918e;
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
					- m_SourcePort = 48 40866 ;
					- m_TargetPort = 48 40866 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 31662c90-23b1-4208-8ef2-01b5a93d764a;
				}
				{ CGIMscMessage 
					- _id = GUID d8b5e709-1ccf-44c5-91ff-dda44f18918e;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 078d3631-eb0f-4c0f-b7e6-259fd0aa02a0;
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
					- m_pSource = GUID dedd2c0a-c9ed-4fb8-930f-3f12fae542d6;
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
					- m_SourcePort = 48 29181 ;
					- m_TargetPort = 48 29185 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID e245815a-2389-46c6-9f3c-975db95b5231;
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
					- m_arrow = 2 1557 1083  1557 1103  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 31503 ;
					- m_TargetPort = 48 32113 ;
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
					- m_SourcePort = 48 43519 ;
					- m_TargetPort = 48 43519 ;
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
					- m_arrow = 2 1003 837  1003 857  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 24001 ;
					- m_TargetPort = 48 24611 ;
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
					- m_SourcePort = 48 45318 ;
					- m_TargetPort = 48 45318 ;
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
					- m_SourcePort = 48 30893 ;
					- m_TargetPort = 48 30893 ;
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
					- m_arrow = 2 774 493  774 526  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 13510 ;
					- m_TargetPort = 48 14516 ;
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
					- m_TargetPort = 48 3324 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 4d1dc794-62e0-4ae5-afcf-8f02d9e198c7;
					- m_pTargetExec = GUID fefd3f91-0624-4889-be9e-ea6a02c65a13;
				}
				{ CGIMscMessage 
					- _id = GUID c7917d82-1e3c-41b0-b715-6c08dab70831;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c996f524-b224-4f1b-bd70-8211f15246bc;
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
					- m_pSource = GUID dedd2c0a-c9ed-4fb8-930f-3f12fae542d6;
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
					- m_SourcePort = 48 11770 ;
					- m_TargetPort = 48 11772 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 9ccf7fdc-2284-4999-863c-fefa1fce0272;
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
					- m_arrow = 2 774 341  774 402  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 8875 ;
					- m_TargetPort = 48 10735 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID c1b8431a-fbc1-4af2-aad0-4bbff6351244;
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
					- m_arrow = 2 1003 725  1003 786  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 20585 ;
					- m_TargetPort = 48 22446 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 950cacc4-3a78-4ce9-81ba-485962a8a989;
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
					- m_arrow = 2 774 552  774 573  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 15309 ;
					- m_TargetPort = 48 15950 ;
					- m_bLeft = 0;
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
					- m_SourcePort = 48 7228 ;
					- m_TargetPort = 48 7228 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 11dc6346-eecf-4aba-b16b-6dbd7e81e2fe;
				}
				{ CGIMscMessage 
					- _id = GUID b351b9a0-a212-4377-b735-87671be14a7c;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c8b53771-fa53-4f61-96d8-ecdc1efe8e09;
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
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID dedd2c0a-c9ed-4fb8-930f-3f12fae542d6;
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
					- m_SourcePort = 48 39823 ;
					- m_TargetPort = 48 39829 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 4c380929-a031-46fb-bc03-9115b4cee956;
					- m_pTargetExec = GUID 463687fc-00f6-4f9f-8128-ecd4539964f3;
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
					- m_SourcePort = 48 8112 ;
					- m_TargetPort = 48 8112 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID ff71f2cd-76de-4d34-9855-94df084450e7;
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
					- m_SourcePort = 48 6160 ;
					- m_TargetPort = 48 6160 ;
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
						- m_str = "Open_lesson_form(Lesson)";
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
					- m_arrow = 2 1334 915  1334 954  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 26380 ;
					- m_TargetPort = 48 27569 ;
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
					- m_SourcePort = 48 44495 ;
					- m_TargetPort = 48 44495 ;
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
					- m_SourcePort = 48 41811 ;
					- m_TargetPort = 48 41811 ;
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
					- m_SourcePort = 48 16560 ;
					- m_TargetPort = 48 16560 ;
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
					- m_SourcePort = 48 35803 ;
					- m_TargetPort = 48 35803 ;
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
					- m_SourcePort = 48 18237 ;
					- m_TargetPort = 48 18237 ;
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
					- m_arrow = 2 1557 1163  1557 1183  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 33943 ;
					- m_TargetPort = 48 34553 ;
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
						- m_str = "Open_lesson_form(Lesson)";
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
					- m_SourcePort = 48 25678 ;
					- m_TargetPort = 48 25678 ;
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
					- m_SourcePort = 48 37297 ;
					- m_TargetPort = 48 37297 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 5883c7d1-f91d-4857-864e-10e1861fef90;
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
					- m_SourcePort = 48 19945 ;
					- m_TargetPort = 48 19945 ;
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
					- m_SourcePort = 48 5337 ;
					- m_TargetPort = 48 5337 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID eff9c99d-f3a6-47b5-917d-3265235fdae3;
					- m_pTargetExec = GUID e93b2a50-67a1-40c7-a0d6-f0bf3944ff43;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 463687fc-00f6-4f9f-8128-ecd4539964f3;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 46c1f84a-a8a7-4b5a-b08d-060bc518fb1b;
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
					- m_transform = 0.442396 0 0 59.2991 45.102 39828.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b351b9a0-a212-4377-b735-87671be14a7c;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 4c380929-a031-46fb-bc03-9115b4cee956;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID f801bc2c-3ed4-450c-a85b-047bbde20353;
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
					- m_transform = 0.721803 0 0 30.4924 43.4547 39823 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b351b9a0-a212-4377-b735-87671be14a7c;
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
				- _objectCreation = "320740116201721-3874123";
				- _umlDependencyID = "1521";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 9;
					- value = 
					{ IClassifierRole 
						- _id = GUID 1df0b941-f3b3-42b4-b0d4-1e8058496769;
						- _name = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _objectCreation = "320742116201721-3876123";
						- _umlDependencyID = "1525";
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
							- _id = GUID 897bea32-c27a-43fe-b2e4-fdd78255e3b9;
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
						- _objectCreation = "320744116201721-3878123";
						- _umlDependencyID = "1529";
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
						- _objectCreation = "320746116201721-3880123";
						- _umlDependencyID = "1524";
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
						- _objectCreation = "320748116201721-3882123";
						- _umlDependencyID = "1528";
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
						- _objectCreation = "320750116201721-3884123";
						- _umlDependencyID = "1523";
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
						- _objectCreation = "320752116201721-3886123";
						- _umlDependencyID = "1527";
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
						- _objectCreation = "320754116201721-3888123";
						- _umlDependencyID = "1531";
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
						- _objectCreation = "320756116201721-3890123";
						- _umlDependencyID = "1526";
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
						- _objectCreation = "320758116201721-3892123";
						- _umlDependencyID = "1530";
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
					- size = 28;
					- value = 
					{ IMessage 
						- _id = GUID 1162968a-36fc-4c53-b888-49f3c2388ad9;
						- _name = "Log_in_user";
						- _objectCreation = "320760116201721-3894123";
						- _umlDependencyID = "2667";
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
							- _name = "Log_in_user()";
							- _id = GUID 0e26fb95-f04b-403a-903b-ff0e7b8a3978;
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
						- _objectCreation = "320762116201721-3896123";
						- _umlDependencyID = "2671";
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
						- _objectCreation = "320764116201721-3898123";
						- _umlDependencyID = "3307";
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
						- _objectCreation = "320766116201721-3900123";
						- _umlDependencyID = "3323";
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
						- _objectCreation = "320768116201721-3902123";
						- _umlDependencyID = "3327";
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
						- _objectCreation = "320770116201721-3904123";
						- _umlDependencyID = "3838";
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
						- _id = GUID 4666f6a6-20e4-476d-aa32-968b58bb2b85;
						- _name = "Update_action_form";
						- _objectCreation = "320772116201721-3906123";
						- _umlDependencyID = "3397";
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
						- _objectCreation = "320774116201721-3908123";
						- _umlDependencyID = "4115";
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
						- _objectCreation = "320776116201721-3910123";
						- _umlDependencyID = "2564";
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
						- _objectCreation = "320778116201721-3912123";
						- _umlDependencyID = "2568";
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
						- _objectCreation = "320780116201721-3914123";
						- _umlDependencyID = "3862";
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
						- _objectCreation = "320782116201721-3916123";
						- _umlDependencyID = "3866";
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
						- _objectCreation = "320784116201721-3918123";
						- _umlDependencyID = "2892";
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
						- _myState = 8192;
						- _name = "Open_lesson_form";
						- _objectCreation = "320786116201721-3920123";
						- _umlDependencyID = "3211";
						- m_szSequence = "15.";
						- m_szActualArgs = "Lesson";
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
						- _myState = 8192;
						- _name = "Open_lesson_form";
						- _objectCreation = "320788116201721-3922123";
						- _umlDependencyID = "3215";
						- m_szSequence = "16.";
						- m_szActualArgs = "Lesson";
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
						- _id = GUID ffae52ad-ab99-4ca7-9093-13ac206e0200;
						- _name = "Open_present_list_form";
						- _objectCreation = "320790116201721-3924123";
						- _umlDependencyID = "3858";
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
						- _objectCreation = "320792116201721-3926123";
						- _umlDependencyID = "3862";
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
						- _objectCreation = "320794116201721-3928123";
						- _umlDependencyID = "4234";
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
						- _objectCreation = "320796116201721-3930123";
						- _umlDependencyID = "2683";
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
						- _objectCreation = "320798116201721-3932123";
						- _umlDependencyID = "2687";
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
						- _objectCreation = "320800116201721-3934123";
						- _umlDependencyID = "2774";
						- m_szSequence = "24.";
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
						- _objectCreation = "320802116201721-3936123";
						- _umlDependencyID = "3062";
						- m_szSequence = "25.";
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
						- _objectCreation = "320804116201721-3938123";
						- _umlDependencyID = "4074";
						- m_szSequence = "28.";
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
						- _objectCreation = "320806116201721-3940123";
						- _umlDependencyID = "3829";
						- m_szSequence = "26.";
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
						- _objectCreation = "320808116201721-3942123";
						- _umlDependencyID = "3958";
						- m_szSequence = "27.";
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
					{ IMessage 
						- _id = GUID c996f524-b224-4f1b-bd70-8211f15246bc;
						- _myState = 8192;
						- _name = "Choose_action";
						- _objectCreation = "320810116201721-3944123";
						- _umlDependencyID = "2859";
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
							- _id = GUID 1df0b941-f3b3-42b4-b0d4-1e8058496769;
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
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID e8461f9c-7e71-4df6-9ff8-cb00c3d5f7d8;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 746142de-b021-40b1-92bd-6f425d6c75b2;
						}
					}
					{ IMessage 
						- _id = GUID 078d3631-eb0f-4c0f-b7e6-259fd0aa02a0;
						- _name = "Set_lesson_info";
						- _objectCreation = "320812116201721-3946123";
						- _umlDependencyID = "3099";
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
							- _id = GUID 1df0b941-f3b3-42b4-b0d4-1e8058496769;
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
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID db72f90f-3b15-41eb-ae90-13a6a28aa452;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 7c4daa2a-3029-40ad-b1e3-9d734d1f9c4e;
						}
					}
					{ IMessage 
						- _id = GUID c8b53771-fa53-4f61-96d8-ecdc1efe8e09;
						- _name = "Mark_present";
						- _objectCreation = "320814116201721-3948123";
						- _umlDependencyID = "2784";
						- m_szSequence = "23.";
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
							- _id = GUID 1df0b941-f3b3-42b4-b0d4-1e8058496769;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "PresentListForm";
							- _name = "Mark_present()";
							- _id = GUID ea2cfc35-ae83-4db0-a18e-5fe76057427e;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 46c1f84a-a8a7-4b5a-b08d-060bc518fb1b;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID f801bc2c-3ed4-450c-a85b-047bbde20353;
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 39;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 53184907-3e44-4f48-a59b-22043416bfc5;
						- _objectCreation = "320816116201721-3950123";
						- _umlDependencyID = "1520";
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
						- _objectCreation = "320818116201721-3952123";
						- _umlDependencyID = "1524";
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
						- _objectCreation = "320820116201721-3954123";
						- _umlDependencyID = "1519";
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
						- _objectCreation = "320822116201721-3956123";
						- _umlDependencyID = "1523";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 9f4e4e93-519b-4f26-a933-64b77b4a1146;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 98;
					}
					{ IExecutionOccurrence 
						- _id = GUID d2c722b7-24cc-46f8-8bef-332aed24a0b4;
						- _objectCreation = "320824116201721-3958123";
						- _umlDependencyID = "1527";
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
						- _objectCreation = "320826116201721-3960123";
						- _umlDependencyID = "1522";
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
						- _objectCreation = "320828116201721-3962123";
						- _umlDependencyID = "1526";
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
						- _objectCreation = "320830116201721-3964123";
						- _umlDependencyID = "1521";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 51a923f4-a441-4a67-9cbd-624010c16afd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 7ed9a8fc-4118-4f6a-baa8-60db72d99030;
						- _objectCreation = "320832116201721-3966123";
						- _umlDependencyID = "1525";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d8d3664c-df5b-4833-bcbf-6e62729cd618;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 227;
					}
					{ IExecutionOccurrence 
						- _id = GUID 662e301a-95fc-4ba9-86af-ecf6e96c55f3;
						- _objectCreation = "320834116201721-3968123";
						- _umlDependencyID = "1529";
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
						- _objectCreation = "320836116201721-3970123";
						- _umlDependencyID = "1524";
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
						- _objectCreation = "320838116201721-3972123";
						- _umlDependencyID = "1528";
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
						- _id = GUID 0d38cfdf-9aab-4d7c-b7b3-10f83670f51c;
						- _objectCreation = "320840116201721-3974123";
						- _umlDependencyID = "1523";
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
						- _objectCreation = "320842116201721-3976123";
						- _umlDependencyID = "1527";
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
						- _objectCreation = "320844116201721-3978123";
						- _umlDependencyID = "1531";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 605d9c34-621f-4a88-a69d-455a4c3ab246;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 75d9e189-05e8-4f1f-80b1-55581cdc8a36;
						- _objectCreation = "320846116201721-3980123";
						- _umlDependencyID = "1526";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 67947061-feae-482f-aef7-f497aa0a11cd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 142;
					}
					{ IExecutionOccurrence 
						- _id = GUID 14434c37-5cfe-4c09-a9e3-51c8b391d687;
						- _objectCreation = "320848116201721-3982123";
						- _umlDependencyID = "1530";
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
						- _objectCreation = "320850116201721-3984123";
						- _umlDependencyID = "1525";
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
						- _objectCreation = "320852116201721-3986123";
						- _umlDependencyID = "1529";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID e3b84458-9107-4206-b873-1bc0209added;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 145;
					}
					{ IExecutionOccurrence 
						- _id = GUID 1e8f4d1c-b739-486c-9d48-ac812efea75a;
						- _objectCreation = "320854116201721-3988123";
						- _umlDependencyID = "1533";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID ffae52ad-ab99-4ca7-9093-13ac206e0200;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 197;
					}
					{ IExecutionOccurrence 
						- _id = GUID 0f6dfd04-cb5f-41cc-8738-2a3b444d8722;
						- _objectCreation = "320856116201721-3990123";
						- _umlDependencyID = "1528";
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
						- _objectCreation = "320858116201721-3992123";
						- _umlDependencyID = "1532";
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
						- _objectCreation = "320860116201721-3994123";
						- _umlDependencyID = "1527";
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
						- _objectCreation = "320862116201721-3996123";
						- _umlDependencyID = "1531";
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
						- _objectCreation = "320864116201721-3998123";
						- _umlDependencyID = "1535";
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
						- _objectCreation = "320866116201721-4000123";
						- _umlDependencyID = "1512";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID cf85f063-c8b3-4ce2-af50-9be1b5981cf1;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 70;
					}
					{ IExecutionOccurrence 
						- _id = GUID 32387afc-7418-4333-8eea-130014ab7cfa;
						- _objectCreation = "320868116201721-4002123";
						- _umlDependencyID = "1516";
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
						- _objectCreation = "320870116201721-4004123";
						- _umlDependencyID = "1511";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a3c624f8-c4a1-4765-a76d-ef48df7de367;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 145;
					}
					{ IExecutionOccurrence 
						- _id = GUID 88674537-2f18-4283-98a3-37c41e00a0ca;
						- _objectCreation = "320872116201721-4006123";
						- _umlDependencyID = "1515";
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
						- _objectCreation = "320874116201721-4008123";
						- _umlDependencyID = "1519";
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
						- _objectCreation = "320876116201721-4010123";
						- _umlDependencyID = "1514";
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
						- _objectCreation = "320878116201721-4012123";
						- _umlDependencyID = "1518";
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
						- _objectCreation = "320880116201721-4014123";
						- _umlDependencyID = "1513";
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
						- _id = GUID e8461f9c-7e71-4df6-9ff8-cb00c3d5f7d8;
						- _objectCreation = "320882116201721-4016123";
						- _umlDependencyID = "1517";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c996f524-b224-4f1b-bd70-8211f15246bc;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 746142de-b021-40b1-92bd-6f425d6c75b2;
						- _objectCreation = "320884116201721-4018123";
						- _umlDependencyID = "1521";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c996f524-b224-4f1b-bd70-8211f15246bc;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID db72f90f-3b15-41eb-ae90-13a6a28aa452;
						- _objectCreation = "320886116201721-4020123";
						- _umlDependencyID = "1516";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 078d3631-eb0f-4c0f-b7e6-259fd0aa02a0;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 7c4daa2a-3029-40ad-b1e3-9d734d1f9c4e;
						- _objectCreation = "320888116201721-4022123";
						- _umlDependencyID = "1520";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 078d3631-eb0f-4c0f-b7e6-259fd0aa02a0;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 46c1f84a-a8a7-4b5a-b08d-060bc518fb1b;
						- _objectCreation = "320890116201721-4024123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c8b53771-fa53-4f61-96d8-ecdc1efe8e09;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 70;
					}
					{ IExecutionOccurrence 
						- _id = GUID f801bc2c-3ed4-450c-a85b-047bbde20353;
						- _objectCreation = "320892116201721-4026123";
						- _umlDependencyID = "1519";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c8b53771-fa53-4f61-96d8-ecdc1efe8e09;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 339d23e4-c68e-4c4c-a4a4-7ee9b46e727f;
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
			- _name = "Add_student_mark";
			- _objectCreation = "320894116201721-4028123";
			- _umlDependencyID = "3180";
			- _lastModifiedTime = "12.11.2017::14:0:54";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID ea31c088-2901-4520-a049-fb0ee078920d;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 339d23e4-c68e-4c4c-a4a4-7ee9b46e727f;
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
				- elementList = 55;
				{ CGIBox 
					- _id = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 0bff9f63-b6c1-4e82-9893-3646c9876e65;
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
					- _id = GUID 615ccf73-f072-42d4-8e2d-0b674f7e05b9;
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 27bf8298-0631-4bc9-9e5b-c34fe9871fb7;
					}
					- m_pParent = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
					- m_name = { CGIText 
						- m_str = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü:\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
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
					- _id = GUID 2f32ec65-c1df-47e5-a0d6-4bb7b1f1e624;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID c77864f3-c664-484b-8c3d-8fd264537309;
					}
					- m_pParent = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
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
					- m_transform = 1.85417 0 0 0.0327904 149 50 ;
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
					- _id = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
					}
					- m_pParent = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
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
					- m_transform = 2.32292 0 0 0.0327904 349 50 ;
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
					- _id = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
					}
					- m_pParent = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
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
					- m_transform = 2.11458 0 0 0.0327904 590 50 ;
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
					- _id = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 4d499bc6-5fbf-43b3-b93d-3e81ec5cf624;
					}
					- m_pParent = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
					- m_name = { CGIText 
						- m_str = "\Ñ\ï\è\ñ\î\ê \ñ\ò\ó\ä\å\í\ò\î\â:StudentsListForm";
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
					- m_transform = 2.22916 0 0 0.0327904 803 50 ;
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
					- _id = GUID 1820a01f-3cec-44cb-ad9f-2d6cb4995038;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 7f97a46e-b810-4a40-8de6-614ccd6a3dea;
					}
					- m_pParent = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
					- m_name = { CGIText 
						- m_str = "\Ñ\ò\ó\ä\å\í\ò:Student";
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
					- m_transform = 0.8125 0 0 0.0327904 1027 50 ;
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
					- _id = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID e3345535-2bde-4940-aaf5-664c826c68bd;
					}
					- m_pParent = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
					- m_name = { CGIText 
						- m_str = "\È\í\ô\î\ð\ì\à\ö\è\ÿ \î\á \î\ö\å\í\ê\å:MarkInfoForm";
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
					- m_transform = 2.15625 0 0 0.0327954 1115 50 ;
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
					- _id = GUID 3799b6a3-ed26-43a5-8319-ec88e7e2b033;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 0602888e-33ca-4b0b-ade3-cd1d17b6fe93;
					}
					- m_pParent = GUID 2f32ec65-c1df-47e5-a0d6-4bb7b1f1e624;
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
					- m_transform = 0.539324 0 0 30.4967 44.8706 3324.14 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b3d75ee0-445f-4c41-b420-5952a72e2811;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 23792112-198b-46a6-9cf7-772156ee4d7a;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 3183dce6-99a3-4964-8e2f-7bab1c7f5976;
					}
					- m_pParent = GUID 2f32ec65-c1df-47e5-a0d6-4bb7b1f1e624;
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
					- m_transform = 0.539324 0 0 96.5729 44.8706 6312.82 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b4d8a6fb-9596-46d1-baca-33e22350ebc5;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID f3694239-76ae-4a23-a786-7dc4961c940a;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID e0d03cc1-6783-4157-bba9-29e34265f5af;
					}
					- m_pParent = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_transform = 0.430493 0 0 30.4967 44.995 6312.82 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b4d8a6fb-9596-46d1-baca-33e22350ebc5;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID db57d61d-15bf-478a-a8cb-91ddbc0be9c6;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 29c3bed7-b4e7-4bd7-b950-861693e72459;
					}
					- m_pParent = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_transform = 0.430493 0 0 51.675 44.995 8691.56 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID dd6ce71e-5d89-465a-878f-61a9356c0224;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 61c84479-94ab-4ceb-88ac-99541d41d91f;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID f6b65277-2f29-46d5-b956-73bd2f535a62;
					}
					- m_pParent = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_transform = 0.472907 0 0 34.7324 44.8563 9453.98 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 05721d36-da1b-4ad6-a6db-a4710421a4d7;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID ae4f22ae-2114-46de-8328-9aed32ce4d57;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID d26a678b-b1bc-4f80-a89c-04f4cd4c6ed3;
					}
					- m_pParent = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_transform = 0.472906 0 0 42.3565 44.8563 14272.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 849d9dec-2959-4c0b-b8fd-5f4702df8eec;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 0d8cda58-8533-46ef-a1e9-50796068f50d;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 4236d389-04b2-4e67-adaf-171c9725cef2;
					}
					- m_pParent = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_transform = 0.472907 0 0 32.191 44.8563 12046.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID fd78a427-59dd-41af-a633-7f50d9cac152;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID c44b304b-edde-4621-9693-e6fd5990dab8;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID d1687db4-a43a-4775-b446-16145bdd4ddb;
					}
					- m_pParent = GUID 615ccf73-f072-42d4-8e2d-0b674f7e05b9;
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
					- m_transform = 0.755903 0 0 30.4924 43.0865 14270.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 849d9dec-2959-4c0b-b8fd-5f4702df8eec;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID b291aacd-d1cc-4611-9e5b-3c43e04bf3c8;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID be99a5d8-1e82-4d5b-a854-869e2e4d7190;
					}
					- m_pParent = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_transform = 0.472907 0 0 94.0315 44.8563 17139.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9f06f61d-bd66-457e-bb41-281cfdcb4139;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID c7106670-2158-4833-bf6d-4d7e9cb59582;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 47d7293c-5e2f-47c3-9edb-6747bc4a831e;
					}
					- m_pParent = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_transform = 0.430493 0 0 87.2544 44.995 19426.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID aec27467-c06a-4712-8d20-13aaebb1c65b;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 7922fd0e-f377-4bab-9206-8086e10a783f;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 7d297458-4571-41c8-abab-1cb007ceeef6;
					}
					- m_pParent = GUID 1820a01f-3cec-44cb-ad9f-2d6cb4995038;
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
					- m_transform = 1.23077 0 0 30.4967 41.0589 21469.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8fbc3a80-63f7-4184-a09b-89fd901c8c15;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 07a4d1a4-611f-413b-acbb-62b9da25bfd0;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 249d6c97-2cca-48e6-a32d-f0efb0242947;
					}
					- m_pParent = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_transform = 0.472907 0 0 30.4967 44.8563 22964 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 0ba68d3d-6bc9-4119-a345-d338d6fbf513;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 8b616be1-797a-4229-bae2-cb1ec166c7ab;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c0355ece-ac09-4fd2-a29c-8d27f6c0073d;
					}
					- m_pParent = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
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
					- m_transform = 0.448599 0 0 40.6623 45.4146 22964 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 0ba68d3d-6bc9-4119-a345-d338d6fbf513;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID ea17753b-7660-4efe-89a1-c18131ce6333;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 6824e60d-e037-4e5e-857f-31b0cd377e9b;
					}
					- m_pParent = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
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
					- m_transform = 0.448599 0 0 107.586 45.4146 25800.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 10d76dce-e59a-4ee0-8bb4-652424b48bbd;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 18c3e9e0-52e4-4e1f-983a-d8e331573bb6;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 94f48fde-6e92-4698-b6ef-e057dae2847f;
					}
					- m_pParent = GUID 615ccf73-f072-42d4-8e2d-0b674f7e05b9;
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
					- m_transform = 0.755903 0 0 30.4924 43.0865 3323.67 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b3d75ee0-445f-4c41-b420-5952a72e2811;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 40867e6a-2f45-4d79-aba9-ff8ce1909edf;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 28be0f06-e3f4-4e79-9892-d7f3f6b57b4a;
					}
					- m_pParent = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_transform = 0.463768 0 0 51.6671 44.8925 30400.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 0097d1d7-72b7-48c7-b9d7-ab4c6c5f5e5b;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 3c57860c-8cdd-4912-8ca0-2b59ee49651e;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 4e7ec5b6-4c6c-4bb4-8a63-572841a7391f;
					}
					- m_pParent = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_transform = 0.463768 0 0 33.8801 44.8925 28571.1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 006cec0d-12e5-4be7-918d-eef6786b9d4d;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID cf29c7ae-889b-440f-958e-cb5f6d726f54;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 34d3893f-c5e3-4ba5-9bae-00347fc23668;
					}
					- m_pParent = GUID 615ccf73-f072-42d4-8e2d-0b674f7e05b9;
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
					- m_transform = 0.755903 0 0 30.4924 43.0865 31163.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 7e561339-863e-4c95-9a89-0c0051972b06;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID dc9db0fc-6db9-4bd2-85ed-8ce997a4a701;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 012aa581-647c-48ee-b139-7c3efe8f11a7;
					}
					- m_pParent = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_transform = 0.463768 0 0 30.4921 44.8925 33602.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 3467f882-faf9-4a46-8589-23c00ca70143;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID df3ce0b4-d33a-4b48-b25f-2d231fd2808d;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID f8886ddf-fd63-4418-b900-3ec62b650f23;
					}
					- m_pParent = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_transform = 0.430494 0 0 87.2544 44.995 33607.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 3467f882-faf9-4a46-8589-23c00ca70143;
				}
				{ CGIMscMessage 
					- _id = GUID 51c8dd53-7be9-4c60-a271-acee3780b7e9;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5916f9d0-43c5-451b-9eed-3a97019f2e9b;
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
					- m_pSource = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_arrow = 2 746 638  746 657  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 17932 ;
					- m_TargetPort = 48 18512 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 8fbc3a80-63f7-4184-a09b-89fd901c8c15;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID f7b4223a-684f-448e-8cc0-39b9798e52d4;
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
					- m_pSource = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1820a01f-3cec-44cb-ad9f-2d6cb4995038;
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
					- m_SourcePort = 48 21470 ;
					- m_TargetPort = 48 21470 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID f63aae06-557b-4ec0-82d6-332016f5d8fb;
					- m_pTargetExec = GUID 7922fd0e-f377-4bab-9206-8086e10a783f;
				}
				{ CGIMscMessage 
					- _id = GUID aec27467-c06a-4712-8d20-13aaebb1c65b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 10979268-3dd3-4ca2-9b80-c6a63ead6095;
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
						- m_position = 4 -25 -9  133 -9  133 10  -25 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 409 664 ;
						- m_nHorizontalSpacing = -3;
						- m_nVerticalSpacing = -3;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_SourcePort = 48 19426 ;
					- m_TargetPort = 48 19426 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 0f1282ff-c510-4050-8323-d0ef1bea0f24;
					- m_pTargetExec = GUID c7106670-2158-4833-bf6d-4d7e9cb59582;
				}
				{ CGIMscMessage 
					- _id = GUID 3467f882-faf9-4a46-8589-23c00ca70143;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 39f86754-ff4d-4080-ab68-a97e4e795764;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Add_mark_info(Mark_info)";
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
					- m_pSource = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
					- m_sourceType = 'F';
					- m_pTarget = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_SourcePort = 48 33602 ;
					- m_TargetPort = 48 33607 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID dc9db0fc-6db9-4bd2-85ed-8ce997a4a701;
					- m_pTargetExec = GUID df3ce0b4-d33a-4b48-b25f-2d231fd2808d;
				}
				{ CGIMscMessage 
					- _id = GUID 10d76dce-e59a-4ee0-8bb4-652424b48bbd;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d964d824-d7e8-4dbb-857a-58809a50f3c5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_students_list_form()";
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
					- m_pSource = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
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
					- m_arrow = 2 966 831  966 896  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 23818 ;
					- m_TargetPort = 48 25800 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID ea17753b-7660-4efe-89a1-c18131ce6333;
				}
				{ CGIMscMessage 
					- _id = GUID 849d9dec-2959-4c0b-b8fd-5f4702df8eec;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 08f7435c-7ebe-41ad-b016-feb1c753fa82;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_action(\"add_student_mark\")";
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
					- m_pSource = GUID 615ccf73-f072-42d4-8e2d-0b674f7e05b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_SourcePort = 48 14270 ;
					- m_TargetPort = 48 14272 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID c44b304b-edde-4621-9693-e6fd5990dab8;
					- m_pTargetExec = GUID ae4f22ae-2114-46de-8328-9aed32ce4d57;
				}
				{ CGIMscMessage 
					- _id = GUID 0097d1d7-72b7-48c7-b9d7-ab4c6c5f5e5b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 38a5aaed-1258-41bb-9bae-14d008614928;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_mark_form(Student_info)";
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
					- m_pSource = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_arrow = 2 1283 1007  1283 1047  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 29181 ;
					- m_TargetPort = 48 30401 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 40867e6a-2f45-4d79-aba9-ff8ce1909edf;
				}
				{ CGIMscMessage 
					- _id = GUID 05721d36-da1b-4ad6-a6db-a4710421a4d7;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID abc9b63a-3017-4b34-8d33-aa84c103ab76;
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
					- m_pSource = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
					- m_sourceType = 'F';
					- m_pTarget = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_SourcePort = 48 9454 ;
					- m_TargetPort = 48 9454 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID b22c6cce-a16c-4690-b3af-b9e8eb596e6a;
					- m_pTargetExec = GUID 61c84479-94ab-4ceb-88ac-99541d41d91f;
				}
				{ CGIMscMessage 
					- _id = GUID e470906c-4ac6-496c-b012-1bfa9f5cb6e8;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID cdcde126-cb1c-490f-96b2-196ca57d9d85;
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
					- m_pSource = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2f32ec65-c1df-47e5-a0d6-4bb7b1f1e624;
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
					- m_SourcePort = 48 7197 ;
					- m_TargetPort = 48 7197 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID b3d75ee0-445f-4c41-b420-5952a72e2811;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 82f86079-b02f-44d6-a071-f173cc8653e1;
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
					- m_pSource = GUID 615ccf73-f072-42d4-8e2d-0b674f7e05b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2f32ec65-c1df-47e5-a0d6-4bb7b1f1e624;
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
					- m_TargetPort = 48 3324 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 18c3e9e0-52e4-4e1f-983a-d8e331573bb6;
					- m_pTargetExec = GUID 3799b6a3-ed26-43a5-8319-ec88e7e2b033;
				}
				{ CGIMscMessage 
					- _id = GUID dd6ce71e-5d89-465a-878f-61a9356c0224;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5bff7f55-b22c-4ef5-bf25-dce551274999;
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
					- m_pSource = GUID 2f32ec65-c1df-47e5-a0d6-4bb7b1f1e624;
					- m_sourceType = 'F';
					- m_pTarget = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_SourcePort = 48 8692 ;
					- m_TargetPort = 48 8692 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 322997b8-2fdd-484b-839f-a290481a72c2;
					- m_pTargetExec = GUID db57d61d-15bf-478a-a8cb-91ddbc0be9c6;
				}
				{ CGIMscMessage 
					- _id = GUID b4d8a6fb-9596-46d1-baca-33e22350ebc5;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 67905df1-c131-4c31-856f-920068dc69f7;
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
					- m_pSource = GUID 2f32ec65-c1df-47e5-a0d6-4bb7b1f1e624;
					- m_sourceType = 'F';
					- m_pTarget = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_SourcePort = 48 6313 ;
					- m_TargetPort = 48 6313 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 23792112-198b-46a6-9cf7-772156ee4d7a;
					- m_pTargetExec = GUID f3694239-76ae-4a23-a786-7dc4961c940a;
				}
				{ CGIMscMessage 
					- _id = GUID 0af3262f-135c-4295-af88-79da03f968ed;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a21b628d-6b9a-4562-81b2-9680dbbfbb41;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Close_mark_info_form()";
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
					- m_pSource = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
					- m_sourceType = 'F';
					- m_pTarget = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_SourcePort = 48 35651 ;
					- m_TargetPort = 48 35645 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 89b7f7fc-6ee2-417c-8546-90c9c69ca1c7;
					- m_pTargetExec = GUID 229b4187-1609-467c-86ab-1ed2bb415d7f;
				}
				{ CGIMscMessage 
					- _id = GUID ec8cad8c-80fe-4973-881a-f58174c6f564;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a350a18b-9bd4-49e5-883c-217ea81c84f1;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_student(Student)";
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
					- m_pSource = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
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
					- m_arrow = 2 966 925  966 954  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 26685 ;
					- m_TargetPort = 48 27569 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 0ba68d3d-6bc9-4119-a345-d338d6fbf513;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID dc17e134-157b-4ea9-b857-ae04ca33576e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_students_list_form()";
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
					- m_pSource = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
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
					- m_SourcePort = 48 22964 ;
					- m_TargetPort = 48 22964 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 07a4d1a4-611f-413b-acbb-62b9da25bfd0;
					- m_pTargetExec = GUID 8b616be1-797a-4229-bae2-cb1ec166c7ab;
				}
				{ CGIMscMessage 
					- _id = GUID 006cec0d-12e5-4be7-918d-eef6786b9d4d;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 2ed6b191-e712-4396-96eb-bf854ca5731c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_mark_form(Student_info)";
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
					- m_pSource = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
					- m_sourceType = 'F';
					- m_pTarget = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_SourcePort = 48 28575 ;
					- m_TargetPort = 48 28571 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 1d8aad97-96bf-4e3e-844f-fca3d7e10eec;
					- m_pTargetExec = GUID 3c57860c-8cdd-4912-8ca0-2b59ee49651e;
				}
				{ CGIMscMessage 
					- _id = GUID 7e561339-863e-4c95-9a89-0c0051972b06;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 64b040ab-2677-4ac2-a047-b3318782abe0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Set_mark_info()";
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
					- m_pSource = GUID 615ccf73-f072-42d4-8e2d-0b674f7e05b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_SourcePort = 48 31163 ;
					- m_TargetPort = 48 31163 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID cf29c7ae-889b-440f-958e-cb5f6d726f54;
					- m_pTargetExec = GUID aac37b0d-eecd-4cad-a0d5-c34cb268f039;
				}
				{ CGIMscMessage 
					- _id = GUID 9f06f61d-bd66-457e-bb41-281cfdcb4139;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 659ef216-2263-4caa-aecb-4f9e8a8c43a4;
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
					- m_pSource = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_arrow = 2 746 548  746 612  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 15187 ;
					- m_TargetPort = 48 17139 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID b291aacd-d1cc-4611-9e5b-3c43e04bf3c8;
				}
				{ CGIMscMessage 
					- _id = GUID fd78a427-59dd-41af-a633-7f50d9cac152;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 8a8141e7-1c93-46ca-b9cf-280944c2ac81;
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
					- m_pSource = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_arrow = 2 746 381  746 445  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 10094 ;
					- m_TargetPort = 48 12046 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 0d8cda58-8533-46ef-a1e9-50796068f50d;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 229b4187-1609-467c-86ab-1ed2bb415d7f;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 2efbd7db-5d74-470b-84ca-2cb0e214f997;
					}
					- m_pParent = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_transform = 0.463768 0 0 30.4921 44.8925 35645.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 0af3262f-135c-4295-af88-79da03f968ed;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID f63aae06-557b-4ec0-82d6-332016f5d8fb;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID a351d785-7dec-4098-8b66-c82133dd206d;
					}
					- m_pParent = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_transform = 0.430493 0 0 30.4967 45.2018 21469.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8fbc3a80-63f7-4184-a09b-89fd901c8c15;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID b22c6cce-a16c-4690-b3af-b9e8eb596e6a;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 3cb33a00-be9f-412b-a35a-7c0eaa19df05;
					}
					- m_pParent = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_transform = 0.430493 0 0 30.4967 45.2018 9453.98 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 05721d36-da1b-4ad6-a6db-a4710421a4d7;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 89b7f7fc-6ee2-417c-8546-90c9c69ca1c7;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID e816d0e4-0358-48e5-a203-5ad1838640fe;
					}
					- m_pParent = GUID dadfe86b-3222-48b9-9366-f93a0e8910e2;
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
					- m_transform = 0.430493 0 0 30.4967 45.2018 35650.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 0af3262f-135c-4295-af88-79da03f968ed;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 0f1282ff-c510-4050-8323-d0ef1bea0f24;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c65ed911-eb41-4bb2-9248-c88343c71d0b;
					}
					- m_pParent = GUID 05f571fa-cc85-419c-bf5b-f9c34a1a84b5;
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
					- m_transform = 0.472906 0 0 30.4967 44.7739 19426.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID aec27467-c06a-4712-8d20-13aaebb1c65b;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID aac37b0d-eecd-4cad-a0d5-c34cb268f039;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID eaee0d38-03cd-4e37-b4ad-2a352c492a8d;
					}
					- m_pParent = GUID 80081be3-c0cb-4b17-b41d-560c7ea45a1c;
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
					- m_transform = 0.463768 0 0 30.4921 45.1244 31162.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 7e561339-863e-4c95-9a89-0c0051972b06;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 1d8aad97-96bf-4e3e-844f-fca3d7e10eec;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 5078fc8a-68db-438c-a5e1-25d11416e1e9;
					}
					- m_pParent = GUID cfe89f02-5329-4502-a768-7d2456cb5722;
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
					- m_transform = 0.448599 0 0 30.4967 45.4146 28575.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 006cec0d-12e5-4be7-918d-eef6786b9d4d;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 322997b8-2fdd-484b-839f-a290481a72c2;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 1c49d753-6619-4970-aaa5-6e4c862bc508;
					}
					- m_pParent = GUID 2f32ec65-c1df-47e5-a0d6-4bb7b1f1e624;
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
					- m_transform = 0.539324 0 0 30.4967 44.7639 8691.56 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID dd6ce71e-5d89-465a-878f-61a9356c0224;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 95dc4781-8c91-4038-8a5e-8e5f201b92d2;
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
				- _id = GUID 0bff9f63-b6c1-4e82-9893-3646c9876e65;
				- _objectCreation = "320896116201721-4030123";
				- _umlDependencyID = "1518";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 7;
					- value = 
					{ IClassifierRole 
						- _id = GUID 27bf8298-0631-4bc9-9e5b-c34fe9871fb7;
						- _name = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _objectCreation = "320898116201721-4032123";
						- _umlDependencyID = "1522";
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
							- _id = GUID 897bea32-c27a-43fe-b2e4-fdd78255e3b9;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID c77864f3-c664-484b-8c3d-8fd264537309;
						- _name = "\Ô\î\ð\ì\à \à\â\ò\î\ð\è\ç\à\ö\è\è";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e0\\'e2\\'f2\\'ee\\'f0\\'e8\\'e7\\'e0\\'f6\\'e8\\'e8\\par
}
";
						- _objectCreation = "320900116201721-4034123";
						- _umlDependencyID = "1508";
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
						- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
						- _name = "\Ì\å\í\å\ä\æ\å\ð \ò\ð\à\í\ç\à\ê\ö\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'cc\\'ee\\'e4\\'f3\\'eb\\'fc \\'e3\\'eb\\'ee\\'e1\\'e0\\'eb\\'fc\\'ed\\'fb\\'f5 \\'e4\\'e0\\'ed\\'ed\\'fb\\'f5\\par
}
";
						- _objectCreation = "320902116201721-4036123";
						- _umlDependencyID = "1512";
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
						- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
						- _name = "\Ñ\ï\è\ñ\î\ê \ä\å\é\ñ\ò\â\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e2\\'fb\\'e1\\'ee\\'f0\\'e0 \\'e4\\'e5\\'e9\\'f1\\'f2\\'e2\\'e8\\'e9\\par
}
";
						- _objectCreation = "320904116201721-4038123";
						- _umlDependencyID = "1516";
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
						- _id = GUID 4d499bc6-5fbf-43b3-b93d-3e81ec5cf624;
						- _name = "\Ñ\ï\è\ñ\î\ê \ñ\ò\ó\ä\å\í\ò\î\â";
						- _objectCreation = "320906116201721-4040123";
						- _umlDependencyID = "1511";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "StudentsListForm";
							- _id = GUID 409dea9c-1f7f-4a05-aecb-e6dfae918168;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 7f97a46e-b810-4a40-8de6-614ccd6a3dea;
						- _name = "\Ñ\ò\ó\ä\å\í\ò";
						- _objectCreation = "320908116201721-4042123";
						- _umlDependencyID = "1515";
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
					{ IClassifierRole 
						- _id = GUID e3345535-2bde-4940-aaf5-664c826c68bd;
						- _name = "\È\í\ô\î\ð\ì\à\ö\è\ÿ \î\á \î\ö\å\í\ê\å";
						- _objectCreation = "320910116201721-4044123";
						- _umlDependencyID = "1510";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "MarkInfoForm";
							- _id = GUID 37e38709-6c88-4073-b84e-c11706ee7e54;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 19;
					- value = 
					{ IMessage 
						- _id = GUID 82f86079-b02f-44d6-a071-f173cc8653e1;
						- _name = "Log_in_user";
						- _objectCreation = "320912116201721-4046123";
						- _umlDependencyID = "2656";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c77864f3-c664-484b-8c3d-8fd264537309;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 27bf8298-0631-4bc9-9e5b-c34fe9871fb7;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Log_in_user()";
							- _id = GUID 0e26fb95-f04b-403a-903b-ff0e7b8a3978;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 0602888e-33ca-4b0b-ade3-cd1d17b6fe93;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 94f48fde-6e92-4698-b6ef-e057dae2847f;
						}
					}
					{ IMessage 
						- _id = GUID 67905df1-c131-4c31-856f-920068dc69f7;
						- _name = "Log_in_user";
						- _objectCreation = "320914116201721-4048123";
						- _umlDependencyID = "2660";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c77864f3-c664-484b-8c3d-8fd264537309;
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
							- _id = GUID e0d03cc1-6783-4157-bba9-29e34265f5af;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 3183dce6-99a3-4964-8e2f-7bab1c7f5976;
						}
					}
					{ IMessage 
						- _id = GUID cdcde126-cb1c-490f-96b2-196ca57d9d85;
						- _name = "Update_login_form";
						- _objectCreation = "320916116201721-4050123";
						- _umlDependencyID = "3287";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c77864f3-c664-484b-8c3d-8fd264537309;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
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
						- _id = GUID 5bff7f55-b22c-4ef5-bf25-dce551274999;
						- _name = "Show_actions_list";
						- _objectCreation = "320918116201721-4052123";
						- _umlDependencyID = "3321";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c77864f3-c664-484b-8c3d-8fd264537309;
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
							- _id = GUID 29c3bed7-b4e7-4bd7-b950-861693e72459;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 1c49d753-6619-4970-aaa5-6e4c862bc508;
						}
					}
					{ IMessage 
						- _id = GUID abc9b63a-3017-4b34-8d33-aa84c103ab76;
						- _name = "Show_actions_list";
						- _objectCreation = "320920116201721-4054123";
						- _umlDependencyID = "3316";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
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
							- _id = GUID f6b65277-2f29-46d5-b956-73bd2f535a62;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 3cb33a00-be9f-412b-a35a-7c0eaa19df05;
						}
					}
					{ IMessage 
						- _id = GUID 8a8141e7-1c93-46ca-b9cf-280944c2ac81;
						- _name = "Open_actions_list_form";
						- _objectCreation = "320922116201721-4056123";
						- _umlDependencyID = "3836";
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
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
							- _id = GUID 4236d389-04b2-4e67-adaf-171c9725cef2;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 08f7435c-7ebe-41ad-b016-feb1c753fa82;
						- _myState = 8192;
						- _name = "Choose_action";
						- _objectCreation = "320924116201721-4058123";
						- _umlDependencyID = "2862";
						- m_szSequence = "7.";
						- m_szActualArgs = "\"add_student_mark\"";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 27bf8298-0631-4bc9-9e5b-c34fe9871fb7;
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
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID d26a678b-b1bc-4f80-a89c-04f4cd4c6ed3;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID d1687db4-a43a-4775-b446-16145bdd4ddb;
						}
					}
					{ IMessage 
						- _id = GUID 659ef216-2263-4caa-aecb-4f9e8a8c43a4;
						- _name = "Update_action_form";
						- _objectCreation = "320926116201721-4060123";
						- _umlDependencyID = "3390";
						- m_szSequence = "8.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
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
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID be99a5d8-1e82-4d5b-a854-869e2e4d7190;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 5916f9d0-43c5-451b-9eed-3a97019f2e9b;
						- _name = "Synchronize_students_list";
						- _objectCreation = "320928116201721-4062123";
						- _umlDependencyID = "4223";
						- m_szSequence = "9.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Synchronize_students_list()";
							- _id = GUID e2e14efe-effa-44be-b299-158c07a86d05;
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
						- _id = GUID 10979268-3dd3-4ca2-9b80-c6a63ead6095;
						- _myState = 8192;
						- _name = "Get_student";
						- _objectCreation = "320930116201721-4064123";
						- _umlDependencyID = "2672";
						- m_szSequence = "10.";
						- m_szActualArgs = "Student";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
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
							- _id = GUID 47d7293c-5e2f-47c3-9edb-6747bc4a831e;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c65ed911-eb41-4bb2-9248-c88343c71d0b;
						}
					}
					{ IMessage 
						- _id = GUID f7b4223a-684f-448e-8cc0-39b9798e52d4;
						- _myState = 8192;
						- _name = "Get_student";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204{\\*\\fname Arial;}Arial CYR;}}
\\viewkind4\\uc1\\pard\\f0\\fs20\\'c2\\'fb\\'e2\\'e5\\'f1\\'f2\\'e8 \\'f1\\'f2\\'f3\\'e4\\'e5\\'ed\\'f2\\'e0\\par
}
";
						- _objectCreation = "320932116201721-4066123";
						- _umlDependencyID = "2676";
						- m_szSequence = "11.";
						- m_szActualArgs = "Student";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7f97a46e-b810-4a40-8de6-614ccd6a3dea;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
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
							- _id = GUID 7d297458-4571-41c8-abab-1cb007ceeef6;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID a351d785-7dec-4098-8b66-c82133dd206d;
						}
					}
					{ IMessage 
						- _id = GUID dc17e134-157b-4ea9-b857-ae04ca33576e;
						- _name = "Open_students_list_form";
						- _objectCreation = "320934116201721-4068123";
						- _umlDependencyID = "3979";
						- m_szSequence = "12.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 4d499bc6-5fbf-43b3-b93d-3e81ec5cf624;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7e1f3abf-62a0-4e51-844b-bed98a166e8f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "StudentsListForm";
							- _name = "Open_students_list_form()";
							- _id = GUID b910028d-14d7-43be-b8c8-3c8ae070d901;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c0355ece-ac09-4fd2-a29c-8d27f6c0073d;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 249d6c97-2cca-48e6-a32d-f0efb0242947;
						}
					}
					{ IMessage 
						- _id = GUID d964d824-d7e8-4dbb-857a-58809a50f3c5;
						- _name = "Open_students_list_form";
						- _objectCreation = "320936116201721-4070123";
						- _umlDependencyID = "3974";
						- m_szSequence = "13.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 4d499bc6-5fbf-43b3-b93d-3e81ec5cf624;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 4d499bc6-5fbf-43b3-b93d-3e81ec5cf624;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "StudentsListForm";
							- _name = "Open_students_list_form()";
							- _id = GUID b910028d-14d7-43be-b8c8-3c8ae070d901;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 6824e60d-e037-4e5e-857f-31b0cd377e9b;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID a350a18b-9bd4-49e5-883c-217ea81c84f1;
						- _myState = 8192;
						- _name = "Choose_student";
						- _objectCreation = "320938116201721-4072123";
						- _umlDependencyID = "3000";
						- m_szSequence = "14.";
						- m_szActualArgs = "Student";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 4d499bc6-5fbf-43b3-b93d-3e81ec5cf624;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 4d499bc6-5fbf-43b3-b93d-3e81ec5cf624;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "StudentsListForm";
							- _name = "Choose_student()";
							- _id = GUID 88113b35-3144-4193-8d62-7383bcfde210;
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
						- _id = GUID 2ed6b191-e712-4396-96eb-bf854ca5731c;
						- _myState = 8192;
						- _name = "Open_mark_form";
						- _objectCreation = "320940116201721-4074123";
						- _umlDependencyID = "2971";
						- m_szSequence = "15.";
						- m_szActualArgs = "Student_info";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e3345535-2bde-4940-aaf5-664c826c68bd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 4d499bc6-5fbf-43b3-b93d-3e81ec5cf624;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "MarkInfoForm";
							- _name = "Open_mark_form()";
							- _id = GUID 4ef0a9af-7f47-4d0b-8cfb-1183a15dbbe4;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 4e7ec5b6-4c6c-4bb4-8a63-572841a7391f;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 5078fc8a-68db-438c-a5e1-25d11416e1e9;
						}
					}
					{ IMessage 
						- _id = GUID 38a5aaed-1258-41bb-9bae-14d008614928;
						- _myState = 8192;
						- _name = "Open_mark_form";
						- _objectCreation = "320942116201721-4076123";
						- _umlDependencyID = "2975";
						- m_szSequence = "16.";
						- m_szActualArgs = "Student_info";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e3345535-2bde-4940-aaf5-664c826c68bd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e3345535-2bde-4940-aaf5-664c826c68bd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "MarkInfoForm";
							- _name = "Open_mark_form()";
							- _id = GUID 4ef0a9af-7f47-4d0b-8cfb-1183a15dbbe4;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 28be0f06-e3f4-4e79-9892-d7f3f6b57b4a;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 64b040ab-2677-4ac2-a047-b3318782abe0;
						- _name = "Set_mark_info";
						- _objectCreation = "320944116201721-4078123";
						- _umlDependencyID = "2869";
						- m_szSequence = "17.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e3345535-2bde-4940-aaf5-664c826c68bd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 27bf8298-0631-4bc9-9e5b-c34fe9871fb7;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "MarkInfoForm";
							- _name = "Set_mark_info()";
							- _id = GUID cd2c5382-23df-411f-89f8-f6739fee3ad4;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID eaee0d38-03cd-4e37-b4ad-2a352c492a8d;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 34d3893f-c5e3-4ba5-9bae-00347fc23668;
						}
					}
					{ IMessage 
						- _id = GUID 39f86754-ff4d-4080-ab68-a97e4e795764;
						- _myState = 8192;
						- _name = "Add_mark_info";
						- _objectCreation = "320946116201721-4080123";
						- _umlDependencyID = "2829";
						- m_szSequence = "18.";
						- m_szActualArgs = "Mark_info";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e3345535-2bde-4940-aaf5-664c826c68bd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Add_mark_info()";
							- _id = GUID 5f21b1c9-5000-46c7-a4fe-4e7370292cb8;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID f8886ddf-fd63-4418-b900-3ec62b650f23;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 012aa581-647c-48ee-b139-7c3efe8f11a7;
						}
					}
					{ IMessage 
						- _id = GUID a21b628d-6b9a-4562-81b2-9680dbbfbb41;
						- _name = "Close_mark_info_form";
						- _objectCreation = "320948116201721-4082123";
						- _umlDependencyID = "3601";
						- m_szSequence = "19.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e3345535-2bde-4940-aaf5-664c826c68bd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d591892c-8b15-4113-8e71-50504cff20e6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "MarkInfoForm";
							- _name = "Close_mark_info_form()";
							- _id = GUID 54174320-77be-4148-98ac-6ca8981c2ecc;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 2efbd7db-5d74-470b-84ca-2cb0e214f997;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID e816d0e4-0358-48e5-a203-5ad1838640fe;
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 28;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 0602888e-33ca-4b0b-ade3-cd1d17b6fe93;
						- _objectCreation = "320950116201721-4084123";
						- _umlDependencyID = "1518";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 82f86079-b02f-44d6-a071-f173cc8653e1;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 94f48fde-6e92-4698-b6ef-e057dae2847f;
						- _objectCreation = "320952116201721-4086123";
						- _umlDependencyID = "1522";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 82f86079-b02f-44d6-a071-f173cc8653e1;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID e0d03cc1-6783-4157-bba9-29e34265f5af;
						- _objectCreation = "320954116201721-4088123";
						- _umlDependencyID = "1526";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 67905df1-c131-4c31-856f-920068dc69f7;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 3183dce6-99a3-4964-8e2f-7bab1c7f5976;
						- _objectCreation = "320956116201721-4090123";
						- _umlDependencyID = "1521";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 67905df1-c131-4c31-856f-920068dc69f7;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 114;
					}
					{ IExecutionOccurrence 
						- _id = GUID 29c3bed7-b4e7-4bd7-b950-861693e72459;
						- _objectCreation = "320958116201721-4092123";
						- _umlDependencyID = "1525";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 5bff7f55-b22c-4ef5-bf25-dce551274999;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 61;
					}
					{ IExecutionOccurrence 
						- _id = GUID 1c49d753-6619-4970-aaa5-6e4c862bc508;
						- _objectCreation = "320960116201721-4094123";
						- _umlDependencyID = "1520";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 5bff7f55-b22c-4ef5-bf25-dce551274999;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID f6b65277-2f29-46d5-b956-73bd2f535a62;
						- _objectCreation = "320962116201721-4096123";
						- _umlDependencyID = "1524";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID abc9b63a-3017-4b34-8d33-aa84c103ab76;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 41;
					}
					{ IExecutionOccurrence 
						- _id = GUID 3cb33a00-be9f-412b-a35a-7c0eaa19df05;
						- _objectCreation = "320964116201721-4098123";
						- _umlDependencyID = "1528";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID abc9b63a-3017-4b34-8d33-aa84c103ab76;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID d26a678b-b1bc-4f80-a89c-04f4cd4c6ed3;
						- _objectCreation = "320966116201721-4100123";
						- _umlDependencyID = "1514";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 08f7435c-7ebe-41ad-b016-feb1c753fa82;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 50;
					}
					{ IExecutionOccurrence 
						- _id = GUID d1687db4-a43a-4775-b446-16145bdd4ddb;
						- _objectCreation = "320968116201721-4102123";
						- _umlDependencyID = "1518";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 08f7435c-7ebe-41ad-b016-feb1c753fa82;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 4236d389-04b2-4e67-adaf-171c9725cef2;
						- _objectCreation = "320970116201721-4104123";
						- _umlDependencyID = "1513";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 8a8141e7-1c93-46ca-b9cf-280944c2ac81;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 38;
					}
					{ IExecutionOccurrence 
						- _id = GUID be99a5d8-1e82-4d5b-a854-869e2e4d7190;
						- _objectCreation = "320972116201721-4106123";
						- _umlDependencyID = "1517";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 659ef216-2263-4caa-aecb-4f9e8a8c43a4;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 111;
					}
					{ IExecutionOccurrence 
						- _id = GUID 47d7293c-5e2f-47c3-9edb-6747bc4a831e;
						- _objectCreation = "320974116201721-4108123";
						- _umlDependencyID = "1521";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 10979268-3dd3-4ca2-9b80-c6a63ead6095;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 103;
					}
					{ IExecutionOccurrence 
						- _id = GUID c65ed911-eb41-4bb2-9248-c88343c71d0b;
						- _objectCreation = "320976116201721-4110123";
						- _umlDependencyID = "1516";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 10979268-3dd3-4ca2-9b80-c6a63ead6095;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 7d297458-4571-41c8-abab-1cb007ceeef6;
						- _objectCreation = "320978116201721-4112123";
						- _umlDependencyID = "1520";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID f7b4223a-684f-448e-8cc0-39b9798e52d4;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID a351d785-7dec-4098-8b66-c82133dd206d;
						- _objectCreation = "320980116201721-4114123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID f7b4223a-684f-448e-8cc0-39b9798e52d4;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID c0355ece-ac09-4fd2-a29c-8d27f6c0073d;
						- _objectCreation = "320982116201721-4116123";
						- _umlDependencyID = "1519";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID dc17e134-157b-4ea9-b857-ae04ca33576e;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 48;
					}
					{ IExecutionOccurrence 
						- _id = GUID 249d6c97-2cca-48e6-a32d-f0efb0242947;
						- _objectCreation = "320984116201721-4118123";
						- _umlDependencyID = "1523";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID dc17e134-157b-4ea9-b857-ae04ca33576e;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 6824e60d-e037-4e5e-857f-31b0cd377e9b;
						- _objectCreation = "320986116201721-4120123";
						- _umlDependencyID = "1518";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d964d824-d7e8-4dbb-857a-58809a50f3c5;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 127;
					}
					{ IExecutionOccurrence 
						- _id = GUID 4e7ec5b6-4c6c-4bb4-8a63-572841a7391f;
						- _objectCreation = "320988116201721-4122123";
						- _umlDependencyID = "1522";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 2ed6b191-e712-4396-96eb-bf854ca5731c;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 40;
					}
					{ IExecutionOccurrence 
						- _id = GUID 5078fc8a-68db-438c-a5e1-25d11416e1e9;
						- _objectCreation = "320990116201721-4124123";
						- _umlDependencyID = "1517";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 2ed6b191-e712-4396-96eb-bf854ca5731c;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 28be0f06-e3f4-4e79-9892-d7f3f6b57b4a;
						- _objectCreation = "320992116201721-4126123";
						- _umlDependencyID = "1521";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 38a5aaed-1258-41bb-9bae-14d008614928;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 61;
					}
					{ IExecutionOccurrence 
						- _id = GUID eaee0d38-03cd-4e37-b4ad-2a352c492a8d;
						- _objectCreation = "320994116201721-4128123";
						- _umlDependencyID = "1525";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 64b040ab-2677-4ac2-a047-b3318782abe0;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 34d3893f-c5e3-4ba5-9bae-00347fc23668;
						- _objectCreation = "320996116201721-4130123";
						- _umlDependencyID = "1520";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 64b040ab-2677-4ac2-a047-b3318782abe0;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID f8886ddf-fd63-4418-b900-3ec62b650f23;
						- _objectCreation = "320998116201721-4132123";
						- _umlDependencyID = "1524";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 39f86754-ff4d-4080-ab68-a97e4e795764;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 103;
					}
					{ IExecutionOccurrence 
						- _id = GUID 012aa581-647c-48ee-b139-7c3efe8f11a7;
						- _objectCreation = "321000116201721-4134123";
						- _umlDependencyID = "1501";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 39f86754-ff4d-4080-ab68-a97e4e795764;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 2efbd7db-5d74-470b-84ca-2cb0e214f997;
						- _objectCreation = "321002116201721-4136123";
						- _umlDependencyID = "1505";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a21b628d-6b9a-4562-81b2-9680dbbfbb41;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID e816d0e4-0358-48e5-a203-5ad1838640fe;
						- _objectCreation = "321004116201721-4138123";
						- _umlDependencyID = "1509";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a21b628d-6b9a-4562-81b2-9680dbbfbb41;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 290df14d-cb8b-4f97-a16d-4fe4a28f0c4f;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
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
								- _Name = "InteractionOccurrence";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,134";
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
										- _Value = "0,16,230";
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
			- _name = "View_student_schedule";
			- _objectCreation = "321006116201721-4140123";
			- _umlDependencyID = "3725";
			- _lastModifiedTime = "12.11.2017::14:0:54";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID 7368feab-42e9-475e-a739-c2927bd3f67d;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 290df14d-cb8b-4f97-a16d-4fe4a28f0c4f;
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
				- elementList = 39;
				{ CGIBox 
					- _id = GUID f7aeecd2-295d-4db0-a5fd-c4ec4efd10ee;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 64dd76fc-2898-4226-9202-5a7880f719b5;
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
					- _id = GUID 12a0e454-f037-461f-883a-4d06eed69b29;
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID c5733231-79ae-4323-b461-715a8bd34bf5;
					}
					- m_pParent = GUID f7aeecd2-295d-4db0-a5fd-c4ec4efd10ee;
					- m_name = { CGIText 
						- m_str = "\Ñ\ò\ó\ä\å\í\ò:\Ñ\ò\ó\ä\å\í\ò";
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
					- m_transform = 0.916667 0 0 0.0152603 0 50 ;
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
					- _id = GUID 8b99a19a-31e1-4aef-9cb8-a5aefa574ebf;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID acb2faf4-3628-4f5a-8709-0996d0b46463;
					}
					- m_pParent = GUID f7aeecd2-295d-4db0-a5fd-c4ec4efd10ee;
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
					- m_transform = 1.85417 0 0 0.0152929 98 50 ;
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
					- _id = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
					}
					- m_pParent = GUID f7aeecd2-295d-4db0-a5fd-c4ec4efd10ee;
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
					- m_transform = 2.32292 0 0 0.0152929 286 50 ;
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
					- _id = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
					}
					- m_pParent = GUID f7aeecd2-295d-4db0-a5fd-c4ec4efd10ee;
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
					- m_transform = 2.11458 0 0 0.0152929 519 50 ;
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
					- _id = GUID 0265c01a-6218-49df-9dcf-089c17dcfb2c;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 143b7554-b2d4-4fef-99fe-5903cb885e0e;
					}
					- m_pParent = GUID f7aeecd2-295d-4db0-a5fd-c4ec4efd10ee;
					- m_name = { CGIText 
						- m_str = "\Ô\î\ð\ì\à \ð\à\ñ\ï\è\ñ\à\í\è\ÿ:ScheduleForm";
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
					- m_transform = 2.26042 0 0 0.0152952 732 50 ;
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
					- _id = GUID 3509feb4-b276-44c6-8a67-115bc1ceb1c0;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 180ceafb-0d60-4016-874f-e5facf2071ef;
					}
					- m_pParent = GUID 8b99a19a-31e1-4aef-9cb8-a5aefa574ebf;
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
					- m_transform = 0.539325 0 0 65.3901 44.764 6081.28 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 2f76742c-7f6c-4702-bb50-9b91494d6467;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID f34b56a5-2b1c-4e98-b178-dc840251c7b6;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 219d062c-769b-4141-9007-2f3a129387e4;
					}
					- m_pParent = GUID 8b99a19a-31e1-4aef-9cb8-a5aefa574ebf;
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
					- m_transform = 0.539325 0 0 178.006 44.764 10854.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 26b3017c-63a7-4dfb-92bd-abbbec6f8841;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 597d36ac-246d-4b78-82b2-c3d5cc88884b;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 12710b91-fbc2-48ac-a1cf-ab35298c82ba;
					}
					- m_pParent = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_transform = 0.430493 0 0 65.3901 45.2017 10854.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 26b3017c-63a7-4dfb-92bd-abbbec6f8841;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID fd2af8f3-612d-4de7-8ce8-97aed22165bf;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 962c55c4-bae3-4e7a-b9c8-43371cb789dc;
					}
					- m_pParent = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_transform = 0.430493 0 0 107.167 45.2017 14908.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 266e535f-05b4-4fc3-8207-27ff87f3d14e;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID ebe7bd28-c628-4153-81ba-d2f93cd95c72;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 319dfe92-2c1f-4bed-b43b-dc1691bde66b;
					}
					- m_pParent = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_transform = 0.472907 0 0 83.554 44.9262 16412.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID fbc3693c-7ac4-4279-aebc-d2cbfe1117e1;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 271d7ee6-e7ca-47df-a222-64b857ba3868;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 84ae8725-80ea-4075-8f0d-0a25d2518e74;
					}
					- m_pParent = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_transform = 0.472907 0 0 526.753 44.9262 22036.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 68b3ac3b-2b93-419c-af07-293b73493fb1;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 309884e3-204b-46aa-8552-2213188f9fbd;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID eb23c829-8c65-4692-8d89-162b4c13c1c6;
					}
					- m_pParent = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_transform = 0.430493 0 0 116.249 45.2017 32433.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 7c2025ae-cabc-4bef-84a1-d71e413fb97b;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 18b19475-2a0e-482c-8e8b-4f286872cd48;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 118ca88b-0285-42f3-9d47-8ed05f15a569;
					}
					- m_pParent = GUID 12a0e454-f037-461f-883a-4d06eed69b29;
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
					- m_transform = 1.09091 0 0 65.5297 41.4546 23459.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 79ed5347-6758-4e16-bf06-bdf9ee1cb6f4;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 3de4732f-7aa6-4694-bb2d-c5fb61982863;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 3ae7ab90-3f06-4c9f-af71-ca8096c57d98;
					}
					- m_pParent = GUID 12a0e454-f037-461f-883a-4d06eed69b29;
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
					- m_transform = 1.09091 0 0 65.5297 41.4546 38269.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID c68e94fe-2fbe-4211-9846-6ff062ec0e47;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 9b5fb014-1463-47b9-b249-b70bc380daab;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID e51cd9a8-aa36-4ba8-9a87-a3ee1c63ba13;
					}
					- m_pParent = GUID 12a0e454-f037-461f-883a-4d06eed69b29;
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
					- m_transform = 1.09091 0 0 65.5297 41.4546 6094.26 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 2f76742c-7f6c-4702-bb50-9b91494d6467;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 78b4975e-16ad-4db6-8837-809f8f3f4134;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 702c5cb1-092e-4404-8d78-079087ef7ce4;
					}
					- m_pParent = GUID 0265c01a-6218-49df-9dcf-089c17dcfb2c;
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
					- m_transform = 0.442396 0 0 161.634 45.1244 39685.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 58c52818-c48d-4512-a751-0a1c26321df8;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 3078f6c4-0dfa-4467-9c8a-9b39eefb7f25;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c9525b47-1b50-43a0-b56b-e82e5dff3ca6;
					}
					- m_pParent = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_transform = 0.430493 0 0 65.39 45.2017 42111.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 4f949457-38ee-4be0-aa54-9917ee1980d9;
				}
				{ CGIMscMessage 
					- _id = GUID 28bde519-9a63-490a-b155-6d4542e55f03;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 121b1672-0ba4-4cdb-8af3-d01626a3534a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_groups_list()";
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
					- m_pSource = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
					- m_sourceType = 'F';
					- m_pTarget = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_SourcePort = 48 35834 ;
					- m_TargetPort = 48 35834 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 4267985b-c622-4853-be56-a17944313d72;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID ddc3a98c-e3db-43b0-946d-089821ce4fe5;
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
					- m_pSource = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b99a19a-31e1-4aef-9cb8-a5aefa574ebf;
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
					- m_SourcePort = 48 12816 ;
					- m_TargetPort = 48 12816 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 266e535f-05b4-4fc3-8207-27ff87f3d14e;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 282c2902-134c-4a2a-b674-327c87c9036a;
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
					- m_pSource = GUID 8b99a19a-31e1-4aef-9cb8-a5aefa574ebf;
					- m_sourceType = 'F';
					- m_pTarget = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_SourcePort = 48 14909 ;
					- m_TargetPort = 48 14909 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID c9f767e2-b03b-471d-b617-e1249c428b6c;
					- m_pTargetExec = GUID fd2af8f3-612d-4de7-8ce8-97aed22165bf;
				}
				{ CGIMscMessage 
					- _id = GUID c68e94fe-2fbe-4211-9846-6ff062ec0e47;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID dd0a0df8-06c5-405b-99fa-079780bb5532;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_group(Group)";
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
					- m_pSource = GUID 12a0e454-f037-461f-883a-4d06eed69b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_SourcePort = 47 38269 ;
					- m_TargetPort = 48 38188 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 3de4732f-7aa6-4694-bb2d-c5fb61982863;
					- m_pTargetExec = GUID 2ef93539-0609-44ba-b582-7dd62138d825;
				}
				{ CGIMscMessage 
					- _id = GUID 7c2025ae-cabc-4bef-84a1-d71e413fb97b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 77ae2694-27fc-4dc6-afb7-db5139788e5b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_groups_list()";
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
					- m_pSource = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_SourcePort = 48 32433 ;
					- m_TargetPort = 48 32433 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID be6a8c1c-6945-4a3c-a327-2922112ee8e2;
					- m_pTargetExec = GUID 309884e3-204b-46aa-8552-2213188f9fbd;
				}
				{ CGIMscMessage 
					- _id = GUID f3985ea0-65a4-4779-b2c9-617e1a9eeb97;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5071e765-aa1f-4a5b-afad-ffc8b510f34d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Synchronize_groups_list()";
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
					- m_pSource = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
					- m_sourceType = 'F';
					- m_pTarget = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_arrow = 2 650 487  650 522  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 28575 ;
					- m_TargetPort = 48 30864 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 58c52818-c48d-4512-a751-0a1c26321df8;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID cc537b80-bf8d-48c0-8ed7-0213be936ce9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_schedule_form(Group)";
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
					- m_pSource = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 0265c01a-6218-49df-9dcf-089c17dcfb2c;
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
					- m_SourcePort = 48 39692 ;
					- m_TargetPort = 48 39686 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 78b4975e-16ad-4db6-8837-809f8f3f4134;
				}
				{ CGIMscMessage 
					- _id = GUID 68b3ac3b-2b93-419c-af07-293b73493fb1;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 47b2094f-81c4-4afa-9bc5-e92fe5170400;
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
					- m_pSource = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
					- m_sourceType = 'F';
					- m_pTarget = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_arrow = 2 650 327  650 387  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 18113 ;
					- m_TargetPort = 48 22036 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 271d7ee6-e7ca-47df-a222-64b857ba3868;
				}
				{ CGIMscMessage 
					- _id = GUID e60fe1c8-9f49-463c-823c-123ad47206b9;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c5e7eb37-01c3-4867-97ce-f890749d75c6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_schedule_form()";
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
					- m_pSource = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
					- m_sourceType = 'F';
					- m_pTarget = GUID 0265c01a-6218-49df-9dcf-089c17dcfb2c;
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
					- m_SourcePort = 48 44204 ;
					- m_TargetPort = 48 44197 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID fbc3693c-7ac4-4279-aebc-d2cbfe1117e1;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID f8b272f9-4644-4640-8f98-54e9c82fdff1;
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
					- m_pSource = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
					- m_sourceType = 'F';
					- m_pTarget = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_SourcePort = 48 16413 ;
					- m_TargetPort = 48 16413 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID daa327c2-5d0e-4b8a-b8dd-233632f6b57c;
					- m_pTargetExec = GUID ebe7bd28-c628-4153-81ba-d2f93cd95c72;
				}
				{ CGIMscMessage 
					- _id = GUID 26b3017c-63a7-4dfb-92bd-abbbec6f8841;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 743b360a-f4ce-4856-b9ab-554bd62215b8;
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
					- m_pSource = GUID 8b99a19a-31e1-4aef-9cb8-a5aefa574ebf;
					- m_sourceType = 'F';
					- m_pTarget = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_SourcePort = 48 10855 ;
					- m_TargetPort = 48 10855 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID f34b56a5-2b1c-4e98-b178-dc840251c7b6;
					- m_pTargetExec = GUID 597d36ac-246d-4b78-82b2-c3d5cc88884b;
				}
				{ CGIMscMessage 
					- _id = GUID 7ad98267-4d34-4c01-8cef-7e9a398715fb;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 66a26efa-842a-4ebb-91ab-f44dbfaee8c9;
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
					- m_pSource = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
					- m_sourceType = 'F';
					- m_pTarget = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_arrow = 2 650 428  650 458  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 24717 ;
					- m_TargetPort = 48 26679 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 4f949457-38ee-4be0-aa54-9917ee1980d9;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 1242072d-0131-4f46-9c50-9753bec05f00;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_schedule(Group)";
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
					- m_pSource = GUID 0265c01a-6218-49df-9dcf-089c17dcfb2c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_SourcePort = 48 42105 ;
					- m_TargetPort = 48 42111 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 89733670-1d83-408f-84b0-afd83a9dcef1;
					- m_pTargetExec = GUID 3078f6c4-0dfa-4467-9c8a-9b39eefb7f25;
				}
				{ CGIMscMessage 
					- _id = GUID 2f76742c-7f6c-4702-bb50-9b91494d6467;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 7a359618-6c40-4afd-b15b-9ed4be322d22;
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
					- m_pSource = GUID 12a0e454-f037-461f-883a-4d06eed69b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b99a19a-31e1-4aef-9cb8-a5aefa574ebf;
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
					- m_SourcePort = 47 6094 ;
					- m_TargetPort = 48 6081 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 9b5fb014-1463-47b9-b249-b70bc380daab;
					- m_pTargetExec = GUID 3509feb4-b276-44c6-8a67-115bc1ceb1c0;
				}
				{ CGIMscMessage 
					- _id = GUID 79ed5347-6758-4e16-bf06-bdf9ee1cb6f4;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 32003e27-39fd-43de-8ef2-1768867c114f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_action(\"student_schedule\")";
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
					- m_pSource = GUID 12a0e454-f037-461f-883a-4d06eed69b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_SourcePort = 47 23460 ;
					- m_TargetPort = 48 23410 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 18b19475-2a0e-482c-8e8b-4f286872cd48;
					- m_pTargetExec = GUID 8f28be25-17d6-45c8-8be8-ac6e79ad4079;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID c9f767e2-b03b-471d-b617-e1249c428b6c;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID df417a12-a8ee-49cc-b2ab-eaae4b53ce0c;
					}
					- m_pParent = GUID 8b99a19a-31e1-4aef-9cb8-a5aefa574ebf;
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
					- m_transform = 0.539325 0 0 65.3898 44.764 14908.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 266e535f-05b4-4fc3-8207-27ff87f3d14e;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID daa327c2-5d0e-4b8a-b8dd-233632f6b57c;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c770b4b6-24b7-4973-b561-e67c896f7d0b;
					}
					- m_pParent = GUID 089b4bb5-e426-4a3c-824e-a67785355397;
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
					- m_transform = 0.430493 0 0 65.3898 45.2017 16412.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID fbc3693c-7ac4-4279-aebc-d2cbfe1117e1;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID be6a8c1c-6945-4a3c-a327-2922112ee8e2;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 289bf4aa-c631-4152-abd7-585837cb943f;
					}
					- m_pParent = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_transform = 0.472907 0 0 65.3898 44.9262 32433.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 7c2025ae-cabc-4bef-84a1-d71e413fb97b;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 2ef93539-0609-44ba-b582-7dd62138d825;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 60f5c7e8-9cfd-4853-ac2f-921f89a32424;
					}
					- m_pParent = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_transform = 0.472907 0 0 65.3898 44.9262 38187.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID c68e94fe-2fbe-4211-9846-6ff062ec0e47;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 8f28be25-17d6-45c8-8be8-ac6e79ad4079;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID feb61660-d7cf-4cd8-9202-b84054b64f40;
					}
					- m_pParent = GUID d67f5e6d-9bcb-4b2c-82a4-14a5bd85aee1;
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
					- m_transform = 0.472907 0 0 65.3898 44.9262 23409.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 79ed5347-6758-4e16-bf06-bdf9ee1cb6f4;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 89733670-1d83-408f-84b0-afd83a9dcef1;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID d6fb598d-5192-486a-9b76-d5150fac5352;
					}
					- m_pParent = GUID 0265c01a-6218-49df-9dcf-089c17dcfb2c;
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
					- m_transform = 0.442396 0 0 65.38 45.1244 42104.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 4f949457-38ee-4be0-aa54-9917ee1980d9;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID f7aeecd2-295d-4db0-a5fd-c4ec4efd10ee;
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
				- _id = GUID 64dd76fc-2898-4226-9202-5a7880f719b5;
				- _objectCreation = "321008116201721-4142123";
				- _umlDependencyID = "1508";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IClassifierRole 
						- _id = GUID c5733231-79ae-4323-b461-715a8bd34bf5;
						- _name = "\Ñ\ò\ó\ä\å\í\ò";
						- _objectCreation = "321010116201721-4144123";
						- _umlDependencyID = "1503";
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "\Ñ\ò\ó\ä\å\í\ò";
							- _id = GUID 68de63f1-49cb-4752-8c01-6d71a665c56f;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID acb2faf4-3628-4f5a-8709-0996d0b46463;
						- _name = "\Ô\î\ð\ì\à \à\â\ò\î\ð\è\ç\à\ö\è\è";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e0\\'e2\\'f2\\'ee\\'f0\\'e8\\'e7\\'e0\\'f6\\'e8\\'e8\\par
}
";
						- _objectCreation = "321012116201721-4146123";
						- _umlDependencyID = "1507";
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
						- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
						- _name = "\Ì\å\í\å\ä\æ\å\ð \ò\ð\à\í\ç\à\ê\ö\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'cc\\'ee\\'e4\\'f3\\'eb\\'fc \\'e3\\'eb\\'ee\\'e1\\'e0\\'eb\\'fc\\'ed\\'fb\\'f5 \\'e4\\'e0\\'ed\\'ed\\'fb\\'f5\\par
}
";
						- _objectCreation = "321014116201721-4148123";
						- _umlDependencyID = "1511";
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
						- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						- _name = "\Ñ\ï\è\ñ\î\ê \ä\å\é\ñ\ò\â\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e2\\'fb\\'e1\\'ee\\'f0\\'e0 \\'e4\\'e5\\'e9\\'f1\\'f2\\'e2\\'e8\\'e9\\par
}
";
						- _objectCreation = "321016116201721-4150123";
						- _umlDependencyID = "1506";
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
						- _id = GUID 143b7554-b2d4-4fef-99fe-5903cb885e0e;
						- _name = "\Ô\î\ð\ì\à \ð\à\ñ\ï\è\ñ\à\í\è\ÿ";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d0\\'e0\\'f1\\'ef\\'e8\\'f1\\'e0\\'ed\\'e8\\'e5\\par
}
";
						- _objectCreation = "321018116201721-4152123";
						- _umlDependencyID = "1510";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "ScheduleForm";
							- _id = GUID 99e5ae54-6aa0-42b7-adc1-178e76c0683f;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 15;
					- value = 
					{ IMessage 
						- _id = GUID 7a359618-6c40-4afd-b15b-9ed4be322d22;
						- _name = "Log_in_user";
						- _objectCreation = "321020116201721-4154123";
						- _umlDependencyID = "2647";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID acb2faf4-3628-4f5a-8709-0996d0b46463;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c5733231-79ae-4323-b461-715a8bd34bf5;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Log_in_user()";
							- _id = GUID 0e26fb95-f04b-403a-903b-ff0e7b8a3978;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 180ceafb-0d60-4016-874f-e5facf2071ef;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID e51cd9a8-aa36-4ba8-9a87-a3ee1c63ba13;
						}
					}
					{ IMessage 
						- _id = GUID 743b360a-f4ce-4856-b9ab-554bd62215b8;
						- _name = "Log_in_user";
						- _objectCreation = "321022116201721-4156123";
						- _umlDependencyID = "2651";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID acb2faf4-3628-4f5a-8709-0996d0b46463;
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
							- _id = GUID 12710b91-fbc2-48ac-a1cf-ab35298c82ba;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 219d062c-769b-4141-9007-2f3a129387e4;
						}
					}
					{ IMessage 
						- _id = GUID ddc3a98c-e3db-43b0-946d-089821ce4fe5;
						- _name = "Update_login_form";
						- _objectCreation = "321024116201721-4158123";
						- _umlDependencyID = "3287";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID acb2faf4-3628-4f5a-8709-0996d0b46463;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
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
						- _id = GUID 282c2902-134c-4a2a-b674-327c87c9036a;
						- _name = "Show_actions_list";
						- _objectCreation = "321026116201721-4160123";
						- _umlDependencyID = "3312";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID acb2faf4-3628-4f5a-8709-0996d0b46463;
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
							- _id = GUID 962c55c4-bae3-4e7a-b9c8-43371cb789dc;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID df417a12-a8ee-49cc-b2ab-eaae4b53ce0c;
						}
					}
					{ IMessage 
						- _id = GUID f8b272f9-4644-4640-8f98-54e9c82fdff1;
						- _name = "Show_actions_list";
						- _objectCreation = "321028116201721-4162123";
						- _umlDependencyID = "3316";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
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
							- _id = GUID 319dfe92-2c1f-4bed-b43b-dc1691bde66b;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c770b4b6-24b7-4973-b561-e67c896f7d0b;
						}
					}
					{ IMessage 
						- _id = GUID 47b2094f-81c4-4afa-9bc5-e92fe5170400;
						- _name = "Open_actions_list_form";
						- _objectCreation = "321030116201721-4164123";
						- _umlDependencyID = "3827";
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
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
							- _id = GUID 84ae8725-80ea-4075-8f0d-0a25d2518e74;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 32003e27-39fd-43de-8ef2-1768867c114f;
						- _myState = 8192;
						- _name = "Choose_action";
						- _objectCreation = "321032116201721-4166123";
						- _umlDependencyID = "2853";
						- m_szSequence = "7.";
						- m_szActualArgs = "\"student_schedule\"";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c5733231-79ae-4323-b461-715a8bd34bf5;
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
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID feb61660-d7cf-4cd8-9202-b84054b64f40;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 118ca88b-0285-42f3-9d47-8ed05f15a569;
						}
					}
					{ IMessage 
						- _id = GUID 66a26efa-842a-4ebb-91ab-f44dbfaee8c9;
						- _name = "Update_action_form";
						- _objectCreation = "321034116201721-4168123";
						- _umlDependencyID = "3390";
						- m_szSequence = "8.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
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
						- _id = GUID 5071e765-aa1f-4a5b-afad-ffc8b510f34d;
						- _name = "Synchronize_groups_list";
						- _objectCreation = "321036116201721-4170123";
						- _umlDependencyID = "3996";
						- m_szSequence = "9.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Synchronize_groups_list()";
							- _id = GUID 96036464-df2e-47fe-b08e-56783b191ed2;
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
						- _id = GUID 77ae2694-27fc-4dc6-afb7-db5139788e5b;
						- _name = "Get_groups_list";
						- _objectCreation = "321038116201721-4172123";
						- _umlDependencyID = "3108";
						- m_szSequence = "10.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_groups_list()";
							- _id = GUID bdc9c9bf-fb6d-4d89-9aa7-be0268ec74f2;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID eb23c829-8c65-4692-8d89-162b4c13c1c6;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 289bf4aa-c631-4152-abd7-585837cb943f;
						}
					}
					{ IMessage 
						- _id = GUID 121b1672-0ba4-4cdb-8af3-d01626a3534a;
						- _name = "Update_groups_list";
						- _objectCreation = "321040116201721-4174123";
						- _umlDependencyID = "3426";
						- m_szSequence = "11.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Update_groups_list()";
							- _id = GUID 736d2655-5393-421f-a34c-9fa5cd3ecda7;
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
						- _id = GUID dd0a0df8-06c5-405b-99fa-079780bb5532;
						- _myState = 8192;
						- _name = "Choose_group";
						- _objectCreation = "321042116201721-4176123";
						- _umlDependencyID = "2774";
						- m_szSequence = "12.";
						- m_szActualArgs = "Group";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c5733231-79ae-4323-b461-715a8bd34bf5;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ActionsListForm";
							- _name = "Choose_group()";
							- _id = GUID 448532c2-b3e1-4297-bfc7-45437abf649d;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 60f5c7e8-9cfd-4853-ac2f-921f89a32424;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 3ae7ab90-3f06-4c9f-af71-ca8096c57d98;
						}
					}
					{ IMessage 
						- _id = GUID cc537b80-bf8d-48c0-8ed7-0213be936ce9;
						- _myState = 8192;
						- _name = "Open_schedule_form";
						- _objectCreation = "321044116201721-4178123";
						- _umlDependencyID = "3390";
						- m_szSequence = "13.";
						- m_szActualArgs = "Group";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 143b7554-b2d4-4fef-99fe-5903cb885e0e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 211335c7-e59a-4d76-b0f8-073a06091f6e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ScheduleForm";
							- _name = "Open_schedule_form()";
							- _id = GUID 4764ff4c-5f92-49b8-bda1-d276964c5cb1;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 702c5cb1-092e-4404-8d78-079087ef7ce4;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 1242072d-0131-4f46-9c50-9753bec05f00;
						- _myState = 8192;
						- _name = "Get_schedule";
						- _objectCreation = "321046116201721-4180123";
						- _umlDependencyID = "2740";
						- m_szSequence = "14.";
						- m_szActualArgs = "Group";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 143b7554-b2d4-4fef-99fe-5903cb885e0e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_schedule()";
							- _id = GUID 5bd0aed7-d93b-4082-bd10-038edde2ac06;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c9525b47-1b50-43a0-b56b-e82e5dff3ca6;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID d6fb598d-5192-486a-9b76-d5150fac5352;
						}
					}
					{ IMessage 
						- _id = GUID c5e7eb37-01c3-4867-97ce-f890749d75c6;
						- _name = "Update_schedule_form";
						- _objectCreation = "321048116201721-4182123";
						- _umlDependencyID = "3598";
						- m_szSequence = "15.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 143b7554-b2d4-4fef-99fe-5903cb885e0e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8dceaac-9f64-4d29-8461-a68dcc1649a1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Update_schedule_form()";
							- _id = GUID e3b6d1bb-77c8-421b-bc89-8d188defb694;
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 18;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 180ceafb-0d60-4016-874f-e5facf2071ef;
						- _objectCreation = "321050116201721-4184123";
						- _umlDependencyID = "1511";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 7a359618-6c40-4afd-b15b-9ed4be322d22;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID e51cd9a8-aa36-4ba8-9a87-a3ee1c63ba13;
						- _objectCreation = "321052116201721-4186123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 7a359618-6c40-4afd-b15b-9ed4be322d22;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 12710b91-fbc2-48ac-a1cf-ab35298c82ba;
						- _objectCreation = "321054116201721-4188123";
						- _umlDependencyID = "1519";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 743b360a-f4ce-4856-b9ab-554bd62215b8;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 219d062c-769b-4141-9007-2f3a129387e4;
						- _objectCreation = "321056116201721-4190123";
						- _umlDependencyID = "1514";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 743b360a-f4ce-4856-b9ab-554bd62215b8;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 98;
					}
					{ IExecutionOccurrence 
						- _id = GUID 962c55c4-bae3-4e7a-b9c8-43371cb789dc;
						- _objectCreation = "321058116201721-4192123";
						- _umlDependencyID = "1518";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 282c2902-134c-4a2a-b674-327c87c9036a;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 59;
					}
					{ IExecutionOccurrence 
						- _id = GUID df417a12-a8ee-49cc-b2ab-eaae4b53ce0c;
						- _objectCreation = "321060116201721-4194123";
						- _umlDependencyID = "1513";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 282c2902-134c-4a2a-b674-327c87c9036a;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 319dfe92-2c1f-4bed-b43b-dc1691bde66b;
						- _objectCreation = "321062116201721-4196123";
						- _umlDependencyID = "1517";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID f8b272f9-4644-4640-8f98-54e9c82fdff1;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 46;
					}
					{ IExecutionOccurrence 
						- _id = GUID c770b4b6-24b7-4973-b561-e67c896f7d0b;
						- _objectCreation = "321064116201721-4198123";
						- _umlDependencyID = "1521";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID f8b272f9-4644-4640-8f98-54e9c82fdff1;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 84ae8725-80ea-4075-8f0d-0a25d2518e74;
						- _objectCreation = "321066116201721-4200123";
						- _umlDependencyID = "1507";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 47b2094f-81c4-4afa-9bc5-e92fe5170400;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 290;
					}
					{ IExecutionOccurrence 
						- _id = GUID eb23c829-8c65-4692-8d89-162b4c13c1c6;
						- _objectCreation = "321068116201721-4202123";
						- _umlDependencyID = "1511";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 77ae2694-27fc-4dc6-afb7-db5139788e5b;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 64;
					}
					{ IExecutionOccurrence 
						- _id = GUID 289bf4aa-c631-4152-abd7-585837cb943f;
						- _objectCreation = "321070116201721-4204123";
						- _umlDependencyID = "1506";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 77ae2694-27fc-4dc6-afb7-db5139788e5b;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 60f5c7e8-9cfd-4853-ac2f-921f89a32424;
						- _objectCreation = "321072116201721-4206123";
						- _umlDependencyID = "1510";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID dd0a0df8-06c5-405b-99fa-079780bb5532;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 43;
					}
					{ IExecutionOccurrence 
						- _id = GUID 3ae7ab90-3f06-4c9f-af71-ca8096c57d98;
						- _objectCreation = "321074116201721-4208123";
						- _umlDependencyID = "1514";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID dd0a0df8-06c5-405b-99fa-079780bb5532;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID feb61660-d7cf-4cd8-9202-b84054b64f40;
						- _objectCreation = "321076116201721-4210123";
						- _umlDependencyID = "1509";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 32003e27-39fd-43de-8ef2-1768867c114f;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 40;
					}
					{ IExecutionOccurrence 
						- _id = GUID 118ca88b-0285-42f3-9d47-8ed05f15a569;
						- _objectCreation = "321078116201721-4212123";
						- _umlDependencyID = "1513";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 32003e27-39fd-43de-8ef2-1768867c114f;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 702c5cb1-092e-4404-8d78-079087ef7ce4;
						- _objectCreation = "321080116201721-4214123";
						- _umlDependencyID = "1508";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID cc537b80-bf8d-48c0-8ed7-0213be936ce9;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 89;
					}
					{ IExecutionOccurrence 
						- _id = GUID c9525b47-1b50-43a0-b56b-e82e5dff3ca6;
						- _objectCreation = "321082116201721-4216123";
						- _umlDependencyID = "1512";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 1242072d-0131-4f46-9c50-9753bec05f00;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID d6fb598d-5192-486a-9b76-d5150fac5352;
						- _objectCreation = "321084116201721-4218123";
						- _umlDependencyID = "1516";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 1242072d-0131-4f46-9c50-9753bec05f00;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 52;
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 4cdf9fd1-a640-41df-9f38-0b7977fa3141;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
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
				}
			}
			- _name = "View_teacher_schedule";
			- _objectCreation = "321086116201721-4220123";
			- _umlDependencyID = "3689";
			- _lastModifiedTime = "12.11.2017::14:0:54";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID 395924b3-7c8a-4bee-bed6-bc4d0ea5ff97;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 4cdf9fd1-a640-41df-9f38-0b7977fa3141;
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
				- elementList = 33;
				{ CGIBox 
					- _id = GUID 1021f8ca-402f-40ec-92bc-a7b3771ea394;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 82c05024-3b62-4f94-ba94-1032429f158e;
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
					- _id = GUID 0f5d5ca3-6704-411d-9c5d-9ccdbed0db25;
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID ad78565c-6b98-4112-b1e3-c4e0d2c6f836;
					}
					- m_pParent = GUID 1021f8ca-402f-40ec-92bc-a7b3771ea394;
					- m_name = { CGIText 
						- m_str = "\Ñ\ò\ó\ä\å\í\ò:\Ñ\ò\ó\ä\å\í\ò";
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
					- m_transform = 0.802084 0 0 0.0152603 2 50 ;
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
					- _id = GUID eba1f8d8-094b-40e8-bb2a-b88d8f5a27f7;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID ed2dd6eb-46f5-4430-a0af-08eacbb72408;
					}
					- m_pParent = GUID 1021f8ca-402f-40ec-92bc-a7b3771ea394;
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
					- m_transform = 1.85417 0 0 0.0152929 88 50 ;
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
					- _id = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
					}
					- m_pParent = GUID 1021f8ca-402f-40ec-92bc-a7b3771ea394;
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
					- m_transform = 2.32292 0 0 0.0152929 276 50 ;
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
					- _id = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
					}
					- m_pParent = GUID 1021f8ca-402f-40ec-92bc-a7b3771ea394;
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
					- m_transform = 2.11458 0 0 0.0152929 509 50 ;
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
					- _id = GUID 6d785bd0-f0e5-4a06-bd7c-190567905a97;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID f8de7b8b-636b-4112-b552-0948d4cb693e;
					}
					- m_pParent = GUID 1021f8ca-402f-40ec-92bc-a7b3771ea394;
					- m_name = { CGIText 
						- m_str = "\Ô\î\ð\ì\à \ð\à\ñ\ï\è\ñ\à\í\è\ÿ:ScheduleForm";
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
					- m_transform = 2.26042 0 0 0.0152952 722 50 ;
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
					- _id = GUID 0a6c920e-5032-4962-91bf-d7205f9fd05f;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID f69c2766-4700-4c8c-9238-d01e60eb74b6;
					}
					- m_pParent = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
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
					- m_transform = 0.430493 0 0 65.3898 45.2017 42111 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 2c99d032-5455-491e-a468-b96f10ba1c56;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID e1c1ea70-a401-457e-8bb4-1b78583acdbe;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID a3428f4e-6002-4142-9b31-bcc36998ba18;
					}
					- m_pParent = GUID 6d785bd0-f0e5-4a06-bd7c-190567905a97;
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
					- m_transform = 0.442396 0 0 161.634 45.1243 39685.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID f4a1c152-1a40-4c71-b2ef-d8635290c40d;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID bf893bca-7ecf-4323-ada9-6a86a20d767f;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID ee732303-9ca5-4887-9134-c748de5e321a;
					}
					- m_pParent = GUID 0f5d5ca3-6704-411d-9c5d-9ccdbed0db25;
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
					- m_transform = 1.24675 0 0 65.5295 39.3467 38269.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 230611b8-1d4c-43b8-b9a4-3a145a046087;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 958de46d-846a-454e-b275-87b395245aa8;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 1bcc7709-1981-43da-a9cc-65b3d4106449;
					}
					- m_pParent = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
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
					- m_transform = 0.430493 0 0 116.249 45.2017 32433.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 54af1b5a-9eed-4cdc-a4aa-11c1f0bc8a3a;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 20ac8777-4d93-4f5f-9269-8d021a118551;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID fa05df4c-f744-45e0-8c07-67ea5ba8029e;
					}
					- m_pParent = GUID 0f5d5ca3-6704-411d-9c5d-9ccdbed0db25;
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
					- m_transform = 1.24675 0 0 65.5295 39.3467 23459.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8b3d602d-44ad-46b5-a840-0537dbc457ae;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 4e9ece56-22b8-4099-8a61-4b01a1ef9496;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 5833423e-c307-4b69-aaa6-a01e0ce15e1b;
					}
					- m_pParent = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_transform = 0.472907 0 0 526.751 44.9262 22036.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 6936289e-fc33-415b-94f2-3257b9ca3b79;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID f48cc7a0-da3c-495e-9123-f4fecacae6c4;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 10ada860-8ecb-4879-aa3b-1e147bf8e5b9;
					}
					- m_pParent = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_transform = 0.472907 0 0 83.5537 44.9262 16412.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID f0f5bf4b-8c0d-4b5f-ac58-ef7cb0a3cfed;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 7a0bd182-c952-42ee-ac83-fd0c67cc6565;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 33e1fbb9-00b0-4b7a-b1aa-7bd6e23d89e1;
					}
					- m_pParent = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
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
					- m_transform = 0.430493 0 0 107.167 45.2017 14908.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 050a9476-e3d4-4fbf-8356-6e66cc5136d1;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 5be5f556-2438-4c20-a85a-0ac804091d23;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 511c105e-40dd-4db0-b69a-93ed8b9f3fe8;
					}
					- m_pParent = GUID eba1f8d8-094b-40e8-bb2a-b88d8f5a27f7;
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
					- m_transform = 0.539325 0 0 178.006 44.764 10854.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 253c717a-782e-412d-a032-48dc03fede06;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID fee4655d-e6f1-480f-9f8e-1661e9fc4d99;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 424ac919-9df0-48f4-891b-05fdca1549cc;
					}
					- m_pParent = GUID eba1f8d8-094b-40e8-bb2a-b88d8f5a27f7;
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
					- m_transform = 0.539325 0 0 65.3898 44.764 6081.25 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8f5c89f3-ed82-43ae-b791-13d31c12fd69;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID bd0d2175-db1d-4571-a8a9-28b60f2cd745;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 43ee3679-bc84-4a52-b14a-08dd1a676b5f;
					}
					- m_pParent = GUID 0f5d5ca3-6704-411d-9c5d-9ccdbed0db25;
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
					- m_transform = 1.24675 0 0 65.5295 39.3467 6094.25 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 8f5c89f3-ed82-43ae-b791-13d31c12fd69;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 4154acc3-900a-4293-93a2-2b6afe02396a;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c6f02b1c-38e4-4cbc-afde-639804d41903;
					}
					- m_pParent = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
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
					- m_transform = 0.430493 0 0 65.3898 45.2017 10854.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 253c717a-782e-412d-a032-48dc03fede06;
				}
				{ CGIMscMessage 
					- _id = GUID e8fd9e03-93e7-40ee-9db8-1c7959be0790;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3d5f49b1-0d8b-4d8f-be71-1a897af00e45;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_schedule_form()";
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
					- m_pSource = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
					- m_sourceType = 'F';
					- m_pTarget = GUID 6d785bd0-f0e5-4a06-bd7c-190567905a97;
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
					- m_SourcePort = 48 44204 ;
					- m_TargetPort = 48 44197 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 2c99d032-5455-491e-a468-b96f10ba1c56;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d0cce23e-d1da-4de3-b6c0-0d7669837f52;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_schedule(Teacher)";
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
					- m_pSource = GUID 6d785bd0-f0e5-4a06-bd7c-190567905a97;
					- m_sourceType = 'F';
					- m_pTarget = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
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
					- m_SourcePort = 48 42105 ;
					- m_TargetPort = 48 42111 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 0a6c920e-5032-4962-91bf-d7205f9fd05f;
				}
				{ CGIMscMessage 
					- _id = GUID f4a1c152-1a40-4c71-b2ef-d8635290c40d;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4c1c7c1a-9ed2-4191-9cd4-29663786f9bd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_schedule_form(Teacher)";
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
					- m_pSource = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 6d785bd0-f0e5-4a06-bd7c-190567905a97;
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
					- m_SourcePort = 48 39692 ;
					- m_TargetPort = 48 39686 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID e1c1ea70-a401-457e-8bb4-1b78583acdbe;
				}
				{ CGIMscMessage 
					- _id = GUID 230611b8-1d4c-43b8-b9a4-3a145a046087;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 04dbfa1b-dc8f-4b35-9226-dd29ffbad825;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_teacher(Teacher)";
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
					- m_pSource = GUID 0f5d5ca3-6704-411d-9c5d-9ccdbed0db25;
					- m_sourceType = 'F';
					- m_pTarget = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_SourcePort = 47 38269 ;
					- m_TargetPort = 48 38188 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID bf893bca-7ecf-4323-ada9-6a86a20d767f;
				}
				{ CGIMscMessage 
					- _id = GUID fe4be5ce-4f2b-4181-9700-894deb0f66bd;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 83bd48c2-fbf0-4ce5-b51a-f9fe16d4fc5f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_teachers_list()";
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
					- m_pSource = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
					- m_sourceType = 'F';
					- m_pTarget = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_SourcePort = 48 35834 ;
					- m_TargetPort = 48 35834 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 54af1b5a-9eed-4cdc-a4aa-11c1f0bc8a3a;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 691bbd00-7700-4401-969a-95ffc5d84900;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_teachers_list()";
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
					- m_pSource = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
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
					- m_SourcePort = 48 32433 ;
					- m_TargetPort = 48 32433 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 958de46d-846a-454e-b275-87b395245aa8;
				}
				{ CGIMscMessage 
					- _id = GUID 586671fd-16f3-46cf-a2d0-2cc9e0df1807;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 2f67ed0b-9d8e-41bb-9e4d-f4aa7784891f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Synchronize_teachers_list()";
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
					- m_pSource = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
					- m_sourceType = 'F';
					- m_pTarget = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_arrow = 2 640 487  640 522  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 28575 ;
					- m_TargetPort = 48 30864 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID f6451d79-e00e-4235-a038-c05fc4ae4cc8;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 2c9a3fbe-f08e-4c1e-88d6-4406f7985a3b;
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
					- m_pSource = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
					- m_sourceType = 'F';
					- m_pTarget = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_arrow = 2 640 428  640 458  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 24717 ;
					- m_TargetPort = 48 26679 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 8b3d602d-44ad-46b5-a840-0537dbc457ae;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c593c4bf-8ecb-4311-b51f-eebb3ec52f75;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_action(\"teacher_schedule\")";
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
					- m_pSource = GUID 0f5d5ca3-6704-411d-9c5d-9ccdbed0db25;
					- m_sourceType = 'F';
					- m_pTarget = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_SourcePort = 47 23460 ;
					- m_TargetPort = 48 23410 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 20ac8777-4d93-4f5f-9269-8d021a118551;
				}
				{ CGIMscMessage 
					- _id = GUID 6936289e-fc33-415b-94f2-3257b9ca3b79;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 593bb567-1b89-4b35-be03-6056863cada1;
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
					- m_pSource = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
					- m_sourceType = 'F';
					- m_pTarget = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_arrow = 2 640 327  640 387  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 18113 ;
					- m_TargetPort = 48 22036 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 4e9ece56-22b8-4099-8a61-4b01a1ef9496;
				}
				{ CGIMscMessage 
					- _id = GUID f0f5bf4b-8c0d-4b5f-ac58-ef7cb0a3cfed;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a687c970-62b2-401d-99ad-c94ccb550f53;
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
					- m_pSource = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
					- m_sourceType = 'F';
					- m_pTarget = GUID d565d0f0-6ebb-4cf9-a3f9-abdfe83ddc6a;
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
					- m_SourcePort = 48 16413 ;
					- m_TargetPort = 48 16413 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID f48cc7a0-da3c-495e-9123-f4fecacae6c4;
				}
				{ CGIMscMessage 
					- _id = GUID 050a9476-e3d4-4fbf-8356-6e66cc5136d1;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 434d0d14-ed2d-4ed5-94c8-bef5bcadbf2c;
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
					- m_pSource = GUID eba1f8d8-094b-40e8-bb2a-b88d8f5a27f7;
					- m_sourceType = 'F';
					- m_pTarget = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
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
					- m_SourcePort = 48 14909 ;
					- m_TargetPort = 48 14909 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 7a0bd182-c952-42ee-ac83-fd0c67cc6565;
				}
				{ CGIMscMessage 
					- _id = GUID b18538ff-f3c4-4f77-bdef-ced52c1a4760;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3f1a2370-94ee-40e4-bbe0-8cb74a7c6239;
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
					- m_pSource = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
					- m_sourceType = 'F';
					- m_pTarget = GUID eba1f8d8-094b-40e8-bb2a-b88d8f5a27f7;
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
					- m_SourcePort = 48 12816 ;
					- m_TargetPort = 48 12816 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 253c717a-782e-412d-a032-48dc03fede06;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID b7a5ac87-daf6-499f-9878-3c7d89fc709f;
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
					- m_pSource = GUID eba1f8d8-094b-40e8-bb2a-b88d8f5a27f7;
					- m_sourceType = 'F';
					- m_pTarget = GUID 48e93d7d-136c-41be-af1b-e15b1f316c01;
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
					- m_SourcePort = 48 10855 ;
					- m_TargetPort = 48 10855 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 5be5f556-2438-4c20-a85a-0ac804091d23;
					- m_pTargetExec = GUID 4154acc3-900a-4293-93a2-2b6afe02396a;
				}
				{ CGIMscMessage 
					- _id = GUID 8f5c89f3-ed82-43ae-b791-13d31c12fd69;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID b3ba82d3-ed95-4d20-b813-74c5270bcd81;
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
					- m_pSource = GUID 0f5d5ca3-6704-411d-9c5d-9ccdbed0db25;
					- m_sourceType = 'F';
					- m_pTarget = GUID eba1f8d8-094b-40e8-bb2a-b88d8f5a27f7;
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
					- m_SourcePort = 47 6094 ;
					- m_TargetPort = 48 6081 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID bd0d2175-db1d-4571-a8a9-28b60f2cd745;
					- m_pTargetExec = GUID fee4655d-e6f1-480f-9f8e-1661e9fc4d99;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 1021f8ca-402f-40ec-92bc-a7b3771ea394;
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
				- _id = GUID 82c05024-3b62-4f94-ba94-1032429f158e;
				- _objectCreation = "321088116201721-4222123";
				- _umlDependencyID = "1515";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IClassifierRole 
						- _id = GUID ad78565c-6b98-4112-b1e3-c4e0d2c6f836;
						- _name = "\Ñ\ò\ó\ä\å\í\ò";
						- _objectCreation = "321090116201721-4224123";
						- _umlDependencyID = "1510";
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "\Ñ\ò\ó\ä\å\í\ò";
							- _id = GUID 68de63f1-49cb-4752-8c01-6d71a665c56f;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID ed2dd6eb-46f5-4430-a0af-08eacbb72408;
						- _name = "\Ô\î\ð\ì\à \à\â\ò\î\ð\è\ç\à\ö\è\è";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e0\\'e2\\'f2\\'ee\\'f0\\'e8\\'e7\\'e0\\'f6\\'e8\\'e8\\par
}
";
						- _objectCreation = "321092116201721-4226123";
						- _umlDependencyID = "1514";
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
						- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
						- _name = "\Ì\å\í\å\ä\æ\å\ð \ò\ð\à\í\ç\à\ê\ö\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'cc\\'ee\\'e4\\'f3\\'eb\\'fc \\'e3\\'eb\\'ee\\'e1\\'e0\\'eb\\'fc\\'ed\\'fb\\'f5 \\'e4\\'e0\\'ed\\'ed\\'fb\\'f5\\par
}
";
						- _objectCreation = "321094116201721-4228123";
						- _umlDependencyID = "1518";
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
						- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						- _name = "\Ñ\ï\è\ñ\î\ê \ä\å\é\ñ\ò\â\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e2\\'fb\\'e1\\'ee\\'f0\\'e0 \\'e4\\'e5\\'e9\\'f1\\'f2\\'e2\\'e8\\'e9\\par
}
";
						- _objectCreation = "321096116201721-4230123";
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
						- _id = GUID f8de7b8b-636b-4112-b552-0948d4cb693e;
						- _name = "\Ô\î\ð\ì\à \ð\à\ñ\ï\è\ñ\à\í\è\ÿ";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d0\\'e0\\'f1\\'ef\\'e8\\'f1\\'e0\\'ed\\'e8\\'e5\\par
}
";
						- _objectCreation = "321098116201721-4232123";
						- _umlDependencyID = "1517";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "ScheduleForm";
							- _id = GUID 99e5ae54-6aa0-42b7-adc1-178e76c0683f;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 15;
					- value = 
					{ IMessage 
						- _id = GUID b3ba82d3-ed95-4d20-b813-74c5270bcd81;
						- _name = "Log_in_user";
						- _objectCreation = "321100116201721-4234123";
						- _umlDependencyID = "2645";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ed2dd6eb-46f5-4430-a0af-08eacbb72408;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ad78565c-6b98-4112-b1e3-c4e0d2c6f836;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Log_in_user()";
							- _id = GUID 0e26fb95-f04b-403a-903b-ff0e7b8a3978;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 424ac919-9df0-48f4-891b-05fdca1549cc;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 43ee3679-bc84-4a52-b14a-08dd1a676b5f;
						}
					}
					{ IMessage 
						- _id = GUID b7a5ac87-daf6-499f-9878-3c7d89fc709f;
						- _name = "Log_in_user";
						- _objectCreation = "321102116201721-4236123";
						- _umlDependencyID = "2649";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ed2dd6eb-46f5-4430-a0af-08eacbb72408;
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
							- _id = GUID c6f02b1c-38e4-4cbc-afde-639804d41903;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 511c105e-40dd-4db0-b69a-93ed8b9f3fe8;
						}
					}
					{ IMessage 
						- _id = GUID 3f1a2370-94ee-40e4-bbe0-8cb74a7c6239;
						- _name = "Update_login_form";
						- _objectCreation = "321104116201721-4238123";
						- _umlDependencyID = "3285";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ed2dd6eb-46f5-4430-a0af-08eacbb72408;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
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
						- _id = GUID 434d0d14-ed2d-4ed5-94c8-bef5bcadbf2c;
						- _name = "Show_actions_list";
						- _objectCreation = "321106116201721-4240123";
						- _umlDependencyID = "3310";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ed2dd6eb-46f5-4430-a0af-08eacbb72408;
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
							- _id = GUID 33e1fbb9-00b0-4b7a-b1aa-7bd6e23d89e1;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 16a2c3b2-0c68-444f-b2ae-59d46a17f922;
						}
					}
					{ IMessage 
						- _id = GUID a687c970-62b2-401d-99ad-c94ccb550f53;
						- _name = "Show_actions_list";
						- _objectCreation = "321108116201721-4242123";
						- _umlDependencyID = "3314";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
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
							- _id = GUID 10ada860-8ecb-4879-aa3b-1e147bf8e5b9;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 1a70b3f8-848b-483b-b874-c23919827d48;
						}
					}
					{ IMessage 
						- _id = GUID 593bb567-1b89-4b35-be03-6056863cada1;
						- _name = "Open_actions_list_form";
						- _objectCreation = "321110116201721-4244123";
						- _umlDependencyID = "3825";
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
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
							- _id = GUID 5833423e-c307-4b69-aaa6-a01e0ce15e1b;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID c593c4bf-8ecb-4311-b51f-eebb3ec52f75;
						- _myState = 8192;
						- _name = "Choose_action";
						- _objectCreation = "321112116201721-4246123";
						- _umlDependencyID = "2851";
						- m_szSequence = "7.";
						- m_szActualArgs = "\"teacher_schedule\"";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ad78565c-6b98-4112-b1e3-c4e0d2c6f836;
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
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID ddcc9bb2-a272-4a66-946a-30018f63342a;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID fa05df4c-f744-45e0-8c07-67ea5ba8029e;
						}
					}
					{ IMessage 
						- _id = GUID 2c9a3fbe-f08e-4c1e-88d6-4406f7985a3b;
						- _name = "Update_action_form";
						- _objectCreation = "321114116201721-4248123";
						- _umlDependencyID = "3388";
						- m_szSequence = "8.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
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
						- _id = GUID 2f67ed0b-9d8e-41bb-9e4d-f4aa7784891f;
						- _name = "Synchronize_teachers_list";
						- _objectCreation = "321116116201721-4250123";
						- _umlDependencyID = "4169";
						- m_szSequence = "9.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
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
						- _id = GUID 691bbd00-7700-4401-969a-95ffc5d84900;
						- _name = "Get_teachers_list";
						- _objectCreation = "321118116201721-4252123";
						- _umlDependencyID = "3281";
						- m_szSequence = "10.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 1bcc7709-1981-43da-a9cc-65b3d4106449;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID cc1220e6-5e83-4002-8004-25ab5786556f;
						}
					}
					{ IMessage 
						- _id = GUID 83bd48c2-fbf0-4ce5-b51a-f9fe16d4fc5f;
						- _name = "Update_teachers_list";
						- _objectCreation = "321120116201721-4254123";
						- _umlDependencyID = "3599";
						- m_szSequence = "11.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
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
						- _id = GUID 04dbfa1b-dc8f-4b35-9226-dd29ffbad825;
						- _myState = 8192;
						- _name = "Choose_teacher";
						- _objectCreation = "321122116201721-4256123";
						- _umlDependencyID = "2947";
						- m_szSequence = "12.";
						- m_szActualArgs = "Teacher";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ad78565c-6b98-4112-b1e3-c4e0d2c6f836;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 344184d1-31c0-43a4-9dc5-44751cb66a28;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID ee732303-9ca5-4887-9134-c748de5e321a;
						}
					}
					{ IMessage 
						- _id = GUID 4c1c7c1a-9ed2-4191-9cd4-29663786f9bd;
						- _myState = 8192;
						- _name = "Open_schedule_form";
						- _objectCreation = "321124116201721-4258123";
						- _umlDependencyID = "3388";
						- m_szSequence = "13.";
						- m_szActualArgs = "Teacher";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID f8de7b8b-636b-4112-b552-0948d4cb693e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e7c45486-0ade-4e1a-89f9-8b67e301bdcd;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "ScheduleForm";
							- _name = "Open_schedule_form()";
							- _id = GUID 4764ff4c-5f92-49b8-bda1-d276964c5cb1;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID a3428f4e-6002-4142-9b31-bcc36998ba18;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID d0cce23e-d1da-4de3-b6c0-0d7669837f52;
						- _myState = 8192;
						- _name = "Get_schedule";
						- _objectCreation = "321126116201721-4260123";
						- _umlDependencyID = "2738";
						- m_szSequence = "14.";
						- m_szActualArgs = "Teacher";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID f8de7b8b-636b-4112-b552-0948d4cb693e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Get_schedule()";
							- _id = GUID 5bd0aed7-d93b-4082-bd10-038edde2ac06;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID f69c2766-4700-4c8c-9238-d01e60eb74b6;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 8e29fa5c-6232-4865-a0bc-df1ebb24f948;
						}
					}
					{ IMessage 
						- _id = GUID 3d5f49b1-0d8b-4d8f-be71-1a897af00e45;
						- _name = "Update_schedule_form";
						- _objectCreation = "321128116201721-4262123";
						- _umlDependencyID = "3596";
						- m_szSequence = "15.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID f8de7b8b-636b-4112-b552-0948d4cb693e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5f354ab1-918d-48db-bea1-6a04b48c757f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "GlobalDataModule";
							- _name = "Update_schedule_form()";
							- _id = GUID e3b6d1bb-77c8-421b-bc89-8d188defb694;
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 18;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 424ac919-9df0-48f4-891b-05fdca1549cc;
						- _objectCreation = "321130116201721-4264123";
						- _umlDependencyID = "1509";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID b3ba82d3-ed95-4d20-b813-74c5270bcd81;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 43ee3679-bc84-4a52-b14a-08dd1a676b5f;
						- _objectCreation = "321132116201721-4266123";
						- _umlDependencyID = "1513";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID b3ba82d3-ed95-4d20-b813-74c5270bcd81;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID c6f02b1c-38e4-4cbc-afde-639804d41903;
						- _objectCreation = "321134116201721-4268123";
						- _umlDependencyID = "1517";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID b7a5ac87-daf6-499f-9878-3c7d89fc709f;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 511c105e-40dd-4db0-b69a-93ed8b9f3fe8;
						- _objectCreation = "321136116201721-4270123";
						- _umlDependencyID = "1512";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID b7a5ac87-daf6-499f-9878-3c7d89fc709f;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 98;
					}
					{ IExecutionOccurrence 
						- _id = GUID 33e1fbb9-00b0-4b7a-b1aa-7bd6e23d89e1;
						- _objectCreation = "321138116201721-4272123";
						- _umlDependencyID = "1516";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 434d0d14-ed2d-4ed5-94c8-bef5bcadbf2c;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 59;
					}
					{ IExecutionOccurrence 
						- _id = GUID 16a2c3b2-0c68-444f-b2ae-59d46a17f922;
						- _objectCreation = "321140116201721-4274123";
						- _umlDependencyID = "1511";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 434d0d14-ed2d-4ed5-94c8-bef5bcadbf2c;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 10ada860-8ecb-4879-aa3b-1e147bf8e5b9;
						- _objectCreation = "321142116201721-4276123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a687c970-62b2-401d-99ad-c94ccb550f53;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 46;
					}
					{ IExecutionOccurrence 
						- _id = GUID 1a70b3f8-848b-483b-b874-c23919827d48;
						- _objectCreation = "321144116201721-4278123";
						- _umlDependencyID = "1519";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a687c970-62b2-401d-99ad-c94ccb550f53;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 5833423e-c307-4b69-aaa6-a01e0ce15e1b;
						- _objectCreation = "321146116201721-4280123";
						- _umlDependencyID = "1514";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 593bb567-1b89-4b35-be03-6056863cada1;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 290;
					}
					{ IExecutionOccurrence 
						- _id = GUID ddcc9bb2-a272-4a66-946a-30018f63342a;
						- _objectCreation = "321148116201721-4282123";
						- _umlDependencyID = "1518";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c593c4bf-8ecb-4311-b51f-eebb3ec52f75;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 40;
					}
					{ IExecutionOccurrence 
						- _id = GUID fa05df4c-f744-45e0-8c07-67ea5ba8029e;
						- _objectCreation = "321150116201721-4284123";
						- _umlDependencyID = "1513";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c593c4bf-8ecb-4311-b51f-eebb3ec52f75;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 1bcc7709-1981-43da-a9cc-65b3d4106449;
						- _objectCreation = "321152116201721-4286123";
						- _umlDependencyID = "1517";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 691bbd00-7700-4401-969a-95ffc5d84900;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 64;
					}
					{ IExecutionOccurrence 
						- _id = GUID cc1220e6-5e83-4002-8004-25ab5786556f;
						- _objectCreation = "321154116201721-4288123";
						- _umlDependencyID = "1521";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 691bbd00-7700-4401-969a-95ffc5d84900;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 344184d1-31c0-43a4-9dc5-44751cb66a28;
						- _objectCreation = "321156116201721-4290123";
						- _umlDependencyID = "1516";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 04dbfa1b-dc8f-4b35-9226-dd29ffbad825;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 43;
					}
					{ IExecutionOccurrence 
						- _id = GUID ee732303-9ca5-4887-9134-c748de5e321a;
						- _objectCreation = "321158116201721-4292123";
						- _umlDependencyID = "1520";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 04dbfa1b-dc8f-4b35-9226-dd29ffbad825;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID a3428f4e-6002-4142-9b31-bcc36998ba18;
						- _objectCreation = "321160116201721-4294123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 4c1c7c1a-9ed2-4191-9cd4-29663786f9bd;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 89;
					}
					{ IExecutionOccurrence 
						- _id = GUID f69c2766-4700-4c8c-9238-d01e60eb74b6;
						- _objectCreation = "321162116201721-4296123";
						- _umlDependencyID = "1519";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d0cce23e-d1da-4de3-b6c0-0d7669837f52;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 8e29fa5c-6232-4865-a0bc-df1ebb24f948;
						- _objectCreation = "321164116201721-4298123";
						- _umlDependencyID = "1523";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d0cce23e-d1da-4de3-b6c0-0d7669837f52;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 52;
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 97bc5141-1233-4ac9-a3b1-2aabe28063b2;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
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
				}
			}
			- _name = "Sign_in_enrollee";
			- _objectCreation = "321166116201721-4300123";
			- _umlDependencyID = "3169";
			- _lastModifiedTime = "12.11.2017::13:58:54";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID b550a0fd-74e5-4696-9f78-1d3f19406922;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 97bc5141-1233-4ac9-a3b1-2aabe28063b2;
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
				{ CGIBox 
					- _id = GUID 2bcff314-9a74-41ea-97f9-19aabe63e743;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 8e66c7a8-796e-4b28-82d2-470337ea36da;
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
					- _id = GUID 163ceebf-c146-4d96-899f-7f0be27273ff;
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 1cc4398c-d54e-4dfc-9590-83fed9022162;
					}
					- m_pParent = GUID 2bcff314-9a74-41ea-97f9-19aabe63e743;
					- m_name = { CGIText 
						- m_str = "\À\á\è\ò\ó\ð\è\å\í\ò:\À\á\è\ò\ó\ð\è\å\í\ò";
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
					- m_transform = 1.11458 0 0 0.0155203 0 50 ;
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
					- _id = GUID 6e13279c-f84b-45aa-a98e-e1deaafdf86d;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 179c152a-7b68-41a8-8032-62406785a97b;
					}
					- m_pParent = GUID 2bcff314-9a74-41ea-97f9-19aabe63e743;
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
					- m_transform = 1.97917 0 0 0.0155535 116 50 ;
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
					- _id = GUID ac2ce2ac-fab3-440d-8255-f16187347047;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 03f87e75-2f4c-49b7-8d3f-2efe5756ec00;
					}
					- m_pParent = GUID 2bcff314-9a74-41ea-97f9-19aabe63e743;
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
					- m_transform = 2.45834 0 0 0.0155535 316 50 ;
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
					- _id = GUID a1007dbc-d1ec-4feb-9bb6-71af0bc3962d;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 1e2dc6f2-693e-4aaf-bdfa-ecc956c4a63e;
					}
					- m_pParent = GUID 2bcff314-9a74-41ea-97f9-19aabe63e743;
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
					- m_transform = 2.11458 0 0 0.0155535 562 50 ;
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
					- _id = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
					}
					- m_pParent = GUID 2bcff314-9a74-41ea-97f9-19aabe63e743;
					- m_name = { CGIText 
						- m_str = "\Ô\î\ð\ì\à \ç\à\ÿ\â\ê\è:EnrolleeSignInForm";
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
					- m_transform = 2.26042 0 0 0.0155558 775 50 ;
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
					- _id = GUID 95dd0c78-b092-4fa3-a7fa-584f0d7c6604;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID de4b704d-d054-497f-a77d-167898966ef5;
					}
					- m_pParent = GUID 163ceebf-c146-4d96-899f-7f0be27273ff;
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
					- m_transform = 0.897195 0 0 64.4317 42.1682 7989.53 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b3388fb0-5e26-450f-869b-620f99c9a0e4;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 6bb4ac42-81cc-4e79-809d-483ab4fc3c3c;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 73e2cb51-6051-4956-897f-b9be178a395a;
					}
					- m_pParent = GUID a1007dbc-d1ec-4feb-9bb6-71af0bc3962d;
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
					- m_transform = 0.472907 0 0 110.729 44.9262 7972.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b3388fb0-5e26-450f-869b-620f99c9a0e4;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID e4b72326-e555-40bc-a1f1-2a1c063097eb;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 047126a1-8243-4df3-b58c-9661b12c590c;
					}
					- m_pParent = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_transform = 0.442396 0 0 226.783 45.1243 9642.71 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 128c9581-d125-4583-8d96-ba6bf853b31f;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID b13df1a2-e10a-4f3e-a3f7-e03e2a77df04;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 29194dff-4883-4955-97e0-fcdd19b84ac2;
					}
					- m_pParent = GUID ac2ce2ac-fab3-440d-8255-f16187347047;
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
					- m_transform = 0.406779 0 0 62.5084 45.3938 13437.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9ddf8589-46ed-4f87-a532-073aa9f53f1f;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID a61d50eb-405f-4ab0-99fe-f612792c300f;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 15cedf74-4a7e-4edc-a943-865b93d92f6a;
					}
					- m_pParent = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_transform = 0.442396 0 0 332.138 45.1243 21214.1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID ca54a5fe-e6bd-42ac-8dc9-fbd12f8d9447;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 0dbf4e11-cbce-4c11-a874-82018e1ca38b;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID a2510f50-15d8-4fc9-827f-3e814c2d0cd6;
					}
					- m_pParent = GUID 163ceebf-c146-4d96-899f-7f0be27273ff;
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
					- m_transform = 0.897199 0 0 64.4317 42.1684 23066.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 515b8009-822a-4490-a33e-b67278fd06bc;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 813c15a3-36c6-4334-b2bd-08dc93f30300;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 27772f2c-c246-45b4-9ea4-ae2f0a8791e8;
					}
					- m_pParent = GUID ac2ce2ac-fab3-440d-8255-f16187347047;
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
					- m_transform = 0.406779 0 0 64.2944 45.3938 25010.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 14d117af-3d62-4b5e-a123-f6275b429f04;
				}
				{ CGIMscMessage 
					- _id = GUID 9ddf8589-46ed-4f87-a532-073aa9f53f1f;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e0d76131-dddb-4aef-aed7-7a43df7d402d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Get_courses_list()";
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
					- m_pSource = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
					- m_sourceType = 'F';
					- m_pTarget = GUID ac2ce2ac-fab3-440d-8255-f16187347047;
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
					- m_SourcePort = 48 13436 ;
					- m_TargetPort = 48 13438 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 0daa6cf9-ac21-47b0-b9f6-f1b99f161617;
					- m_pTargetExec = GUID b13df1a2-e10a-4f3e-a3f7-e03e2a77df04;
				}
				{ CGIMscMessage 
					- _id = GUID 515b8009-822a-4490-a33e-b67278fd06bc;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 6254aa05-3df7-4f63-ad2b-b46822d10f1c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Fill_sign_in_form()";
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
					- m_pSource = GUID 163ceebf-c146-4d96-899f-7f0be27273ff;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_SourcePort = 48 23067 ;
					- m_TargetPort = 48 23014 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 0dbf4e11-cbce-4c11-a874-82018e1ca38b;
					- m_pTargetExec = GUID e806b647-f6f1-45b1-873f-b536226808a3;
				}
				{ CGIMscMessage 
					- _id = GUID ca54a5fe-e6bd-42ac-8dc9-fbd12f8d9447;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c4ea4081-a942-4eca-8186-57f168eceb6b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_sign_in_form()";
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
					- m_pSource = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_arrow = 2 913 291  913 380  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 15493 ;
					- m_TargetPort = 48 21214 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID a61d50eb-405f-4ab0-99fe-f612792c300f;
				}
				{ CGIMscMessage 
					- _id = GUID b7558b16-ce92-4691-87bd-e511f11472d7;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 17ed298f-2681-40a6-8a2e-a4b9cb83126a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_sign_in_form()";
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
					- m_pSource = GUID ac2ce2ac-fab3-440d-8255-f16187347047;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_SourcePort = 48 26939 ;
					- m_TargetPort = 48 26935 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 14d117af-3d62-4b5e-a123-f6275b429f04;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID ab868b36-ba15-4ca8-b9e8-4820e3d91e56;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Add_enrollee_request(Info)";
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
					- m_pSource = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
					- m_sourceType = 'F';
					- m_pTarget = GUID ac2ce2ac-fab3-440d-8255-f16187347047;
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
					- m_SourcePort = 48 25007 ;
					- m_TargetPort = 48 25011 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 58664169-90ba-4d4f-b5c1-29a139a41599;
					- m_pTargetExec = GUID 813c15a3-36c6-4334-b2bd-08dc93f30300;
				}
				{ CGIMscMessage 
					- _id = GUID 128c9581-d125-4583-8d96-ba6bf853b31f;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d741e5b1-f0b7-48eb-9975-96bb78129da3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_sign_in_form()";
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
					- m_pSource = GUID a1007dbc-d1ec-4feb-9bb6-71af0bc3962d;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_SourcePort = 48 9644 ;
					- m_TargetPort = 48 9643 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID bc01a7af-c89b-49ea-aa3b-f2fa7716dd77;
					- m_pTargetExec = GUID e4b72326-e555-40bc-a1f1-2a1c063097eb;
				}
				{ CGIMscMessage 
					- _id = GUID b3388fb0-5e26-450f-869b-620f99c9a0e4;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5c0b78f4-8c71-4a10-8dcf-ba6d421c64cb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_action(\"sign_in_enrollee\")";
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
					- m_pSource = GUID 163ceebf-c146-4d96-899f-7f0be27273ff;
					- m_sourceType = 'F';
					- m_pTarget = GUID a1007dbc-d1ec-4feb-9bb6-71af0bc3962d;
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
					- m_SourcePort = 47 7990 ;
					- m_TargetPort = 48 7972 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 95dd0c78-b092-4fa3-a7fa-584f0d7c6604;
					- m_pTargetExec = GUID 6bb4ac42-81cc-4e79-809d-483ab4fc3c3c;
				}
				{ CGIMscMessage 
					- _id = GUID 90ab5718-4a0e-4782-83c2-40b0b7f03e5a;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 90cd6421-672b-44ba-b1c7-7898377bd2fd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_sign_in_form()";
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
					- m_pSource = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_arrow = 2 913 497  913 539  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 28735 ;
					- m_TargetPort = 48 31435 ;
					- m_bLeft = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 0daa6cf9-ac21-47b0-b9f6-f1b99f161617;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 46e4be29-bce6-4a53-96ee-edfc6daf38f4;
					}
					- m_pParent = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_transform = 0.442396 0 0 64.2848 45.1244 13435.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9ddf8589-46ed-4f87-a532-073aa9f53f1f;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 58664169-90ba-4d4f-b5c1-29a139a41599;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 689179e3-f041-43f6-bd44-b3d36ceb8e3e;
					}
					- m_pParent = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_transform = 0.442396 0 0 64.2848 45.1244 25006.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 14d117af-3d62-4b5e-a123-f6275b429f04;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID e806b647-f6f1-45b1-873f-b536226808a3;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID a1ab5085-cf9e-4404-aeda-f70d131ed160;
					}
					- m_pParent = GUID 7977b972-1da8-4aff-b902-6c2e8b6d830b;
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
					- m_transform = 0.442396 0 0 64.2848 45.1244 23013.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 515b8009-822a-4490-a33e-b67278fd06bc;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID bc01a7af-c89b-49ea-aa3b-f2fa7716dd77;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 14ad2c4b-a3b5-4197-a830-1c81f59932c2;
					}
					- m_pParent = GUID a1007dbc-d1ec-4feb-9bb6-71af0bc3962d;
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
					- m_transform = 0.472907 0 0 64.2943 44.9262 9644.14 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 128c9581-d125-4583-8d96-ba6bf853b31f;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 2bcff314-9a74-41ea-97f9-19aabe63e743;
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
				- _id = GUID 8e66c7a8-796e-4b28-82d2-470337ea36da;
				- _objectCreation = "321168116201721-4302123";
				- _umlDependencyID = "1513";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IClassifierRole 
						- _id = GUID 1cc4398c-d54e-4dfc-9590-83fed9022162;
						- _name = "\À\á\è\ò\ó\ð\è\å\í\ò";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d1\\'f2\\'f3\\'e4\\'e5\\'ed\\'f2\\par
}
";
						- _objectCreation = "321170116201721-4304123";
						- _umlDependencyID = "1508";
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "\À\á\è\ò\ó\ð\è\å\í\ò";
							- _id = GUID 6c37dd20-4808-4dd0-beb9-abaf20f8a720;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 179c152a-7b68-41a8-8032-62406785a97b;
						- _name = "\Ô\î\ð\ì\à \à\â\ò\î\ð\è\ç\à\ö\è\è";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e0\\'e2\\'f2\\'ee\\'f0\\'e8\\'e7\\'e0\\'f6\\'e8\\'e8\\par
}
";
						- _objectCreation = "321172116201721-4306123";
						- _umlDependencyID = "1512";
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
						- _id = GUID 03f87e75-2f4c-49b7-8d3f-2efe5756ec00;
						- _name = "\Ì\å\í\å\ä\æ\å\ð \ò\ð\à\í\ç\à\ê\ö\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'cc\\'ee\\'e4\\'f3\\'eb\\'fc \\'e3\\'eb\\'ee\\'e1\\'e0\\'eb\\'fc\\'ed\\'fb\\'f5 \\'e4\\'e0\\'ed\\'ed\\'fb\\'f5\\par
}
";
						- _objectCreation = "321174116201721-4308123";
						- _umlDependencyID = "1516";
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
						- _id = GUID 1e2dc6f2-693e-4aaf-bdfa-ecc956c4a63e;
						- _name = "\Ñ\ï\è\ñ\î\ê \ä\å\é\ñ\ò\â\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e2\\'fb\\'e1\\'ee\\'f0\\'e0 \\'e4\\'e5\\'e9\\'f1\\'f2\\'e2\\'e8\\'e9\\par
}
";
						- _objectCreation = "321176116201721-4310123";
						- _umlDependencyID = "1511";
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
						- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						- _name = "\Ô\î\ð\ì\à \ç\à\ÿ\â\ê\è";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d0\\'e0\\'f1\\'ef\\'e8\\'f1\\'e0\\'ed\\'e8\\'e5\\par
}
";
						- _objectCreation = "321178116201721-4312123";
						- _umlDependencyID = "1515";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "EnrolleeSignInForm";
							- _id = GUID d2d5d89f-25f0-4fd2-a0da-e56c7953e9f6;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 8;
					- value = 
					{ IMessage 
						- _id = GUID 5c0b78f4-8c71-4a10-8dcf-ba6d421c64cb;
						- _myState = 8192;
						- _name = "Choose_action";
						- _objectCreation = "321180116201721-4314123";
						- _umlDependencyID = "2852";
						- m_szSequence = "1.";
						- m_szActualArgs = "\"sign_in_enrollee\"";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1e2dc6f2-693e-4aaf-bdfa-ecc956c4a63e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1cc4398c-d54e-4dfc-9590-83fed9022162;
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
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 73e2cb51-6051-4956-897f-b9be178a395a;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID de4b704d-d054-497f-a77d-167898966ef5;
						}
					}
					{ IMessage 
						- _id = GUID d741e5b1-f0b7-48eb-9975-96bb78129da3;
						- _name = "Open_sign_in_form";
						- _objectCreation = "321182116201721-4316123";
						- _umlDependencyID = "3285";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1e2dc6f2-693e-4aaf-bdfa-ecc956c4a63e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 047126a1-8243-4df3-b58c-9661b12c590c;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 14ad2c4b-a3b5-4197-a830-1c81f59932c2;
						}
					}
					{ IMessage 
						- _id = GUID e0d76131-dddb-4aef-aed7-7a43df7d402d;
						- _name = "Get_courses_list";
						- _objectCreation = "321184116201721-4318123";
						- _umlDependencyID = "3212";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 03f87e75-2f4c-49b7-8d3f-2efe5756ec00;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 29194dff-4883-4955-97e0-fcdd19b84ac2;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 46e4be29-bce6-4a53-96ee-edfc6daf38f4;
						}
					}
					{ IMessage 
						- _id = GUID c4ea4081-a942-4eca-8186-57f168eceb6b;
						- _name = "Update_sign_in_form";
						- _objectCreation = "321186116201721-4320123";
						- _umlDependencyID = "3493";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 15cedf74-4a7e-4edc-a943-865b93d92f6a;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 6254aa05-3df7-4f63-ad2b-b46822d10f1c;
						- _name = "Fill_sign_in_form";
						- _objectCreation = "321188116201721-4322123";
						- _umlDependencyID = "3277";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 1cc4398c-d54e-4dfc-9590-83fed9022162;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID a1ab5085-cf9e-4404-aeda-f70d131ed160;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID a2510f50-15d8-4fc9-827f-3e814c2d0cd6;
						}
					}
					{ IMessage 
						- _id = GUID ab868b36-ba15-4ca8-b9e8-4820e3d91e56;
						- _myState = 8192;
						- _name = "Add_enrollee_request";
						- _objectCreation = "321190116201721-4324123";
						- _umlDependencyID = "3598";
						- m_szSequence = "6.";
						- m_szActualArgs = "Info";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 03f87e75-2f4c-49b7-8d3f-2efe5756ec00;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 27772f2c-c246-45b4-9ea4-ae2f0a8791e8;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 689179e3-f041-43f6-bd44-b3d36ceb8e3e;
						}
					}
					{ IMessage 
						- _id = GUID 17ed298f-2681-40a6-8a2e-a4b9cb83126a;
						- _name = "Update_sign_in_form";
						- _objectCreation = "321192116201721-4326123";
						- _umlDependencyID = "3496";
						- m_szSequence = "7.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 03f87e75-2f4c-49b7-8d3f-2efe5756ec00;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
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
						- _id = GUID 90cd6421-672b-44ba-b1c7-7898377bd2fd;
						- _name = "Update_sign_in_form";
						- _objectCreation = "321194116201721-4328123";
						- _umlDependencyID = "3500";
						- m_szSequence = "8.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 88976dab-af30-45de-bde7-6708c4120c1c;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 11;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 73e2cb51-6051-4956-897f-b9be178a395a;
						- _objectCreation = "321196116201721-4330123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 5c0b78f4-8c71-4a10-8dcf-ba6d421c64cb;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 62;
					}
					{ IExecutionOccurrence 
						- _id = GUID de4b704d-d054-497f-a77d-167898966ef5;
						- _objectCreation = "321198116201721-4332123";
						- _umlDependencyID = "1519";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 5c0b78f4-8c71-4a10-8dcf-ba6d421c64cb;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 047126a1-8243-4df3-b58c-9661b12c590c;
						- _objectCreation = "321200116201721-4334123";
						- _umlDependencyID = "1505";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d741e5b1-f0b7-48eb-9975-96bb78129da3;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 127;
					}
					{ IExecutionOccurrence 
						- _id = GUID 14ad2c4b-a3b5-4197-a830-1c81f59932c2;
						- _objectCreation = "321202116201721-4336123";
						- _umlDependencyID = "1509";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d741e5b1-f0b7-48eb-9975-96bb78129da3;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 29194dff-4883-4955-97e0-fcdd19b84ac2;
						- _objectCreation = "321204116201721-4338123";
						- _umlDependencyID = "1513";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID e0d76131-dddb-4aef-aed7-7a43df7d402d;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 35;
					}
					{ IExecutionOccurrence 
						- _id = GUID 46e4be29-bce6-4a53-96ee-edfc6daf38f4;
						- _objectCreation = "321206116201721-4340123";
						- _umlDependencyID = "1508";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID e0d76131-dddb-4aef-aed7-7a43df7d402d;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 52;
					}
					{ IExecutionOccurrence 
						- _id = GUID 15cedf74-4a7e-4edc-a943-865b93d92f6a;
						- _objectCreation = "321208116201721-4342123";
						- _umlDependencyID = "1512";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c4ea4081-a942-4eca-8186-57f168eceb6b;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 186;
					}
					{ IExecutionOccurrence 
						- _id = GUID a1ab5085-cf9e-4404-aeda-f70d131ed160;
						- _objectCreation = "321210116201721-4344123";
						- _umlDependencyID = "1507";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 6254aa05-3df7-4f63-ad2b-b46822d10f1c;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 51;
					}
					{ IExecutionOccurrence 
						- _id = GUID a2510f50-15d8-4fc9-827f-3e814c2d0cd6;
						- _objectCreation = "321212116201721-4346123";
						- _umlDependencyID = "1511";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 6254aa05-3df7-4f63-ad2b-b46822d10f1c;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 27772f2c-c246-45b4-9ea4-ae2f0a8791e8;
						- _objectCreation = "321214116201721-4348123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID ab868b36-ba15-4ca8-b9e8-4820e3d91e56;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 689179e3-f041-43f6-bd44-b3d36ceb8e3e;
						- _objectCreation = "321216116201721-4350123";
						- _umlDependencyID = "1510";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID ab868b36-ba15-4ca8-b9e8-4820e3d91e56;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 50;
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID cfe53f5b-544b-4bd3-ba0f-472d4db0e457;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
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
				}
			}
			- _name = "Add_notification";
			- _objectCreation = "321218116201721-4352123";
			- _umlDependencyID = "3161";
			- _lastModifiedTime = "12.11.2017::14:4:57";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID f20682ee-f33c-47b3-8d03-1726ee74a3bb;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID cfe53f5b-544b-4bd3-ba0f-472d4db0e457;
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
				- elementList = 32;
				{ CGIBox 
					- _id = GUID 0c4e15bc-f6bb-49ac-8c1e-6a9443202137;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID ec5e2475-6bd7-4018-a590-82f4991253fc;
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
					- _id = GUID 2146fc57-d698-415c-afcf-c50193278016;
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 24fb0545-4d6d-4b8d-832d-933da34a260e;
					}
					- m_pParent = GUID 0c4e15bc-f6bb-49ac-8c1e-6a9443202137;
					- m_name = { CGIText 
						- m_str = "\Ä\å\ê\à\í\à\ò:\Ä\å\ê\à\í\à\ò";
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
					- m_transform = 0.833331 0 0 0.0185204 0 50 ;
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
					- _id = GUID 506786f3-f085-4b1a-a2d2-3f469a3f2776;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 3056f134-6b3f-4558-b4de-174dd9105b4a;
					}
					- m_pParent = GUID 0c4e15bc-f6bb-49ac-8c1e-6a9443202137;
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
					- m_transform = 1.97917 0 0 0.01856 90 50 ;
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
					- _id = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID c43f7998-83ea-4e48-a116-140e2eec421d;
					}
					- m_pParent = GUID 0c4e15bc-f6bb-49ac-8c1e-6a9443202137;
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
					- m_transform = 2.45834 0 0 0.01856 290 50 ;
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
					- _id = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 8feff97b-2ede-41cd-a1dc-e026891207ae;
					}
					- m_pParent = GUID 0c4e15bc-f6bb-49ac-8c1e-6a9443202137;
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
					- m_transform = 2.11458 0 0 0.01856 536 50 ;
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
					- _id = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
					}
					- m_pParent = GUID 0c4e15bc-f6bb-49ac-8c1e-6a9443202137;
					- m_name = { CGIText 
						- m_str = "\Ô\î\ð\ì\à \ï\î\ä\à\÷\è \î\á\ú\â\ë\å\í\è\ÿ:NotifyForm";
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
					- m_transform = 2.26042 0 0 0.0185627 749 50 ;
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
					- _id = GUID 9b91dc27-3607-4e0f-a353-2ad50e8ab2d4;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID a5089d90-fe00-4109-b376-cf136586d46c;
					}
					- m_pParent = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
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
					- m_transform = 0.406779 0 0 53.8794 45.5592 34267.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID e07e524f-52c5-4cef-9028-f2f52631bba3;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 80d46c79-1027-45e9-aa55-9fd6807f2357;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 810c22f1-da1b-442a-88d3-7a5d91ccbcd9;
					}
					- m_pParent = GUID 2146fc57-d698-415c-afcf-c50193278016;
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
					- m_transform = 1.2 0 0 53.9946 40.8001 32666.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID af3c7983-f4a5-4f08-8ebe-a2f7c33aeeb3;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 0f212b9c-ea8a-4790-badb-26e20b0ca563;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID e0c1fe28-a23e-4cb1-9237-1d6d02f734eb;
					}
					- m_pParent = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
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
					- m_transform = 0.442396 0 0 278.336 45.1244 31083.8 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID ca362e7a-0d15-405f-980d-8e2a23621340;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 659773d5-2448-459a-b6e9-beea5c15e2bd;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 76767779-9bcf-4770-8bb0-c9d527747fd5;
					}
					- m_pParent = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
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
					- m_transform = 0.472907 0 0 92.7923 44.9262 19989.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b0b003af-7608-454d-887d-b1e56509f902;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID f1831bb3-35a2-41b8-95a7-0fc004739af2;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 8a449a89-7b81-470d-a165-a098fdcb4068;
					}
					- m_pParent = GUID 2146fc57-d698-415c-afcf-c50193278016;
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
					- m_transform = 1.2 0 0 53.9946 40.8001 20032 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b0b003af-7608-454d-887d-b1e56509f902;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID a934d4fc-8a30-465e-a83c-c1a76166ab65;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 2c55b913-2f0e-43be-83ee-272ae07264ed;
					}
					- m_pParent = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
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
					- m_transform = 0.442396 0 0 210.996 45.1244 21386.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID e77cecaf-4aed-472d-9194-f294eaa25bce;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID b191f901-b8cd-4479-bfdc-3f9034abc9ec;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 1e11dabd-0692-4aa0-9fc7-246e3310550e;
					}
					- m_pParent = GUID 2146fc57-d698-415c-afcf-c50193278016;
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
					- m_transform = 1.2 0 0 53.9946 40.8001 5345.47 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 4b4fadfc-79e0-49c4-afec-b34ef8f51d24;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 12fb94ac-f084-4d5c-a6f4-b2daa7fb242a;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID e95c2fc6-1126-4c05-9dc9-6222b0dd3362;
					}
					- m_pParent = GUID 506786f3-f085-4b1a-a2d2-3f469a3f2776;
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
					- m_transform = 0.505262 0 0 53.8794 44.9683 5334.06 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 4b4fadfc-79e0-49c4-afec-b34ef8f51d24;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 9436342c-8d30-4c4a-935c-3b25255f9074;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID f6298112-f29e-4ba1-86da-7454590cded7;
					}
					- m_pParent = GUID 506786f3-f085-4b1a-a2d2-3f469a3f2776;
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
					- m_transform = 0.505262 0 0 175.108 44.9683 9267.25 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID bdddaee8-0a9e-466f-85c4-d09b45f842ca;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 528a106a-1bc7-4885-81e4-ea7dbdec258c;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 3f919efe-c384-4943-86db-c6138c4a1742;
					}
					- m_pParent = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
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
					- m_transform = 0.406779 0 0 53.8794 45.5592 9267.25 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID bdddaee8-0a9e-466f-85c4-d09b45f842ca;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 727ec7d9-81d6-4d52-b1b3-39e5055550f8;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 0d8a6ec0-734a-493e-94a2-b504c799be76;
					}
					- m_pParent = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
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
					- m_transform = 0.406779 0 0 113.745 45.5592 12553.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 9caa7d8c-596d-4097-bd65-36cede9e08ff;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID f97e46b0-2ad1-4103-a77a-f53d32fea262;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 4464fa2e-60ee-49cb-8738-175f14a341f2;
					}
					- m_pParent = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
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
					- m_transform = 0.472907 0 0 59.866 44.9262 13631.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 46a79d7d-2ca4-4da8-8fa9-789096609cbc;
				}
				{ CGIMscMessage 
					- _id = GUID b8acdb5f-174c-4fe3-a510-10320554a382;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID ac9c03d3-913c-47f4-af85-bf0a73fa0b6f;
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
						- m_position = 4 -38 -9  149 -9  149 10  -38 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 688 323 ;
						- m_nHorizontalSpacing = 13;
						- m_nVerticalSpacing = -9;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
					- m_sourceType = 'F';
					- m_pTarget = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
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
					- m_arrow = 2 667 323  667 374  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 14709 ;
					- m_TargetPort = 48 17457 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID b53e04a8-1a11-4394-96a1-e973935fb15d;
				}
				{ CGIMscMessage 
					- _id = GUID 9ca263b7-41f9-493e-ba67-864ca390b08a;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 57eb8258-0cd5-44b8-a61f-e4c169388f4d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_notify_form()";
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
					- m_pSource = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
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
					- m_arrow = 2 887 744  887 786  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 37387 ;
					- m_TargetPort = 48 39649 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID af3c7983-f4a5-4f08-8ebe-a2f7c33aeeb3;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 6da9589e-d6fc-421b-bd99-c5d799289956;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Fill_notify_form()";
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
					- m_pSource = GUID 2146fc57-d698-415c-afcf-c50193278016;
					- m_sourceType = 'F';
					- m_pTarget = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
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
					- m_SourcePort = 48 32667 ;
					- m_TargetPort = 48 32592 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 80d46c79-1027-45e9-aa55-9fd6807f2357;
				}
				{ CGIMscMessage 
					- _id = GUID bff39add-4c6b-4827-a77b-de66dca2f4ab;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3440f3fc-4cb9-4926-863b-a78d918ec89b;
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
					- m_pSource = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
					- m_sourceType = 'F';
					- m_pTarget = GUID 506786f3-f085-4b1a-a2d2-3f469a3f2776;
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
					- m_SourcePort = 48 10668 ;
					- m_TargetPort = 48 10668 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID ca362e7a-0d15-405f-980d-8e2a23621340;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 74bf59c2-2df5-49b6-a544-5699753b3616;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_notify_form(Author)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -7 -10  165 -10  165 9  -7 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 1.18023 0 0 1.31579 877.262 279.158 ;
						- m_nHorizontalSpacing = 6;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
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
					- m_arrow = 2 887 538  887 627  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 26289 ;
					- m_TargetPort = 48 31084 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 0f212b9c-ea8a-4790-badb-26e20b0ca563;
				}
				{ CGIMscMessage 
					- _id = GUID bdddaee8-0a9e-466f-85c4-d09b45f842ca;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a37e79e5-37c9-4bb1-a4b7-670056771d93;
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
					- m_pSource = GUID 506786f3-f085-4b1a-a2d2-3f469a3f2776;
					- m_sourceType = 'F';
					- m_pTarget = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
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
					- m_SourcePort = 48 9267 ;
					- m_TargetPort = 48 9267 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 9436342c-8d30-4c4a-935c-3b25255f9074;
					- m_pTargetExec = GUID 528a106a-1bc7-4885-81e4-ea7dbdec258c;
				}
				{ CGIMscMessage 
					- _id = GUID b0b003af-7608-454d-887d-b1e56509f902;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4b27784e-02ea-4c3d-96c3-ad5d7692b818;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Choose_action(\"notify\")";
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
					- m_pSource = GUID 2146fc57-d698-415c-afcf-c50193278016;
					- m_sourceType = 'F';
					- m_pTarget = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
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
					- m_SourcePort = 47 20032 ;
					- m_TargetPort = 48 19989 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID f1831bb3-35a2-41b8-95a7-0fc004739af2;
					- m_pTargetExec = GUID 659773d5-2448-459a-b6e9-beea5c15e2bd;
				}
				{ CGIMscMessage 
					- _id = GUID 4b4fadfc-79e0-49c4-afec-b34ef8f51d24;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 20e09dac-0090-41e5-8533-52ab800ccd60;
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
					- m_pSource = GUID 2146fc57-d698-415c-afcf-c50193278016;
					- m_sourceType = 'F';
					- m_pTarget = GUID 506786f3-f085-4b1a-a2d2-3f469a3f2776;
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
					- m_SourcePort = 48 5345 ;
					- m_TargetPort = 48 5334 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID b191f901-b8cd-4479-bfdc-3f9034abc9ec;
					- m_pTargetExec = GUID 12fb94ac-f084-4d5c-a6f4-b2daa7fb242a;
				}
				{ CGIMscMessage 
					- _id = GUID 9caa7d8c-596d-4097-bd65-36cede9e08ff;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 57bafc62-f7c1-4c6c-aa95-aa0e6584a936;
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
					- m_pSource = GUID 506786f3-f085-4b1a-a2d2-3f469a3f2776;
					- m_sourceType = 'F';
					- m_pTarget = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
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
					- m_SourcePort = 48 12554 ;
					- m_TargetPort = 48 12554 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 727ec7d9-81d6-4d52-b1b3-39e5055550f8;
				}
				{ CGIMscMessage 
					- _id = GUID e07e524f-52c5-4cef-9028-f2f52631bba3;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID fd2a6887-3ede-4b80-8123-2609cf303cf9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Add_notification(Info)";
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
					- m_pSource = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
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
					- m_SourcePort = 48 34262 ;
					- m_TargetPort = 48 34267 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 9b91dc27-3607-4e0f-a353-2ad50e8ab2d4;
				}
				{ CGIMscMessage 
					- _id = GUID e77cecaf-4aed-472d-9194-f294eaa25bce;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c1ce6645-9620-443e-9f13-906d3dfc5c89;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Open_notify_form(Author)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -7 -10  153 -10  153 9  -7 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 646 191 ;
						- m_nHorizontalSpacing = -4;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
					- m_sourceType = 'F';
					- m_pTarget = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
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
					- m_SourcePort = 48 21390 ;
					- m_TargetPort = 48 21387 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID a934d4fc-8a30-465e-a83c-c1a76166ab65;
				}
				{ CGIMscMessage 
					- _id = GUID 46a79d7d-2ca4-4da8-8fa9-789096609cbc;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 661bc253-75f4-4767-ae12-326e2c395ffe;
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
					- m_pSource = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
					- m_sourceType = 'F';
					- m_pTarget = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
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
					- m_SourcePort = 48 13631 ;
					- m_TargetPort = 48 13631 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID f97e46b0-2ad1-4103-a77a-f53d32fea262;
				}
				{ CGIMscMessage 
					- _id = GUID f560fd66-111a-4c4d-94b9-e66915924d41;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c836aa64-1ddc-43e1-bb5c-8f1bb699835e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Update_notify_form()";
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
					- m_pSource = GUID 359e50eb-8667-49c1-8378-d1c234f5c1a5;
					- m_sourceType = 'F';
					- m_pTarget = GUID 18474a6a-84ed-4292-8e13-88540b10a6e0;
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
					- m_SourcePort = 48 35884 ;
					- m_TargetPort = 48 35878 ;
					- m_bLeft = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID b53e04a8-1a11-4394-96a1-e973935fb15d;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 3973aaf4-68f3-4ed9-b21a-16eed7b6019e;
					}
					- m_pParent = GUID 31656a41-c266-49f6-a69b-8f65220e2567;
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
					- m_transform = 0.472907 0 0 53.8793 44.9262 17456.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID b8acdb5f-174c-4fe3-a510-10320554a382;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 0c4e15bc-f6bb-49ac-8c1e-6a9443202137;
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
				- _id = GUID ec5e2475-6bd7-4018-a590-82f4991253fc;
				- _objectCreation = "321220116201721-4354123";
				- _umlDependencyID = "1509";
				- ClassifierRoles = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IClassifierRole 
						- _id = GUID 24fb0545-4d6d-4b8d-832d-933da34a260e;
						- _name = "\Ä\å\ê\à\í\à\ò";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d1\\'f2\\'f3\\'e4\\'e5\\'ed\\'f2\\par
}
";
						- _objectCreation = "321222116201721-4356123";
						- _umlDependencyID = "1513";
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "\Ä\å\ê\à\í\à\ò";
							- _id = GUID 39336f2b-c764-4e4c-a704-a05a36ba9f0c;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 3056f134-6b3f-4558-b4de-174dd9105b4a;
						- _name = "\Ô\î\ð\ì\à \à\â\ò\î\ð\è\ç\à\ö\è\è";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e0\\'e2\\'f2\\'ee\\'f0\\'e8\\'e7\\'e0\\'f6\\'e8\\'e8\\par
}
";
						- _objectCreation = "321224116201721-4358123";
						- _umlDependencyID = "1517";
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
						- _id = GUID c43f7998-83ea-4e48-a116-140e2eec421d;
						- _name = "\Ì\å\í\å\ä\æ\å\ð \ò\ð\à\í\ç\à\ê\ö\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'cc\\'ee\\'e4\\'f3\\'eb\\'fc \\'e3\\'eb\\'ee\\'e1\\'e0\\'eb\\'fc\\'ed\\'fb\\'f5 \\'e4\\'e0\\'ed\\'ed\\'fb\\'f5\\par
}
";
						- _objectCreation = "321226116201721-4360123";
						- _umlDependencyID = "1512";
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
						- _id = GUID 8feff97b-2ede-41cd-a1dc-e026891207ae;
						- _name = "\Ñ\ï\è\ñ\î\ê \ä\å\é\ñ\ò\â\è\é";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d4\\'ee\\'f0\\'ec\\'e0 \\'e2\\'fb\\'e1\\'ee\\'f0\\'e0 \\'e4\\'e5\\'e9\\'f1\\'f2\\'e2\\'e8\\'e9\\par
}
";
						- _objectCreation = "321228116201721-4362123";
						- _umlDependencyID = "1516";
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
						- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						- _name = "\Ô\î\ð\ì\à \ï\î\ä\à\÷\è \î\á\ú\â\ë\å\í\è\ÿ";
						- _displayName = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 MS Shell Dlg;}}
\\viewkind4\\uc1\\pard\\f0\\fs16\\'d0\\'e0\\'f1\\'ef\\'e8\\'f1\\'e0\\'ed\\'e8\\'e5\\par
}
";
						- _objectCreation = "321230116201721-4364123";
						- _umlDependencyID = "1511";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "";
							- _name = "NotifyForm";
							- _id = GUID 01dc4b88-a93c-4a54-8723-db777f9f16f4;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 13;
					- value = 
					{ IMessage 
						- _id = GUID 4b27784e-02ea-4c3d-96c3-ad5d7692b818;
						- _myState = 8192;
						- _name = "Choose_action";
						- _objectCreation = "321232116201721-4366123";
						- _umlDependencyID = "2857";
						- m_szSequence = "7.";
						- m_szActualArgs = "\"notify\"";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 8feff97b-2ede-41cd-a1dc-e026891207ae;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 24fb0545-4d6d-4b8d-832d-933da34a260e;
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
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 76767779-9bcf-4770-8bb0-c9d527747fd5;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 8a449a89-7b81-470d-a165-a098fdcb4068;
						}
					}
					{ IMessage 
						- _id = GUID c1ce6645-9620-443e-9f13-906d3dfc5c89;
						- _myState = 8192;
						- _name = "Open_notify_form";
						- _objectCreation = "321234116201721-4368123";
						- _umlDependencyID = "3212";
						- m_szSequence = "8.";
						- m_szActualArgs = "Author";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 8feff97b-2ede-41cd-a1dc-e026891207ae;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "NotifyForm";
							- _name = "Open_notify_form()";
							- _id = GUID 3805868b-23de-425b-8c02-c44aa2a42672;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 2c55b913-2f0e-43be-83ee-272ae07264ed;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 4cae1fb0-d303-462d-890b-e0b729a36a8b;
						}
					}
					{ IMessage 
						- _id = GUID 74bf59c2-2df5-49b6-a544-5699753b3616;
						- _myState = 8192;
						- _name = "Update_notify_form";
						- _objectCreation = "321236116201721-4370123";
						- _umlDependencyID = "3416";
						- m_szSequence = "9.";
						- m_szActualArgs = "Author";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID e0c1fe28-a23e-4cb1-9237-1d6d02f734eb;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 6da9589e-d6fc-421b-bd99-c5d799289956;
						- _name = "Fill_notify_form";
						- _objectCreation = "321238116201721-4372123";
						- _umlDependencyID = "3200";
						- m_szSequence = "10.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 24fb0545-4d6d-4b8d-832d-933da34a260e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID dfb98b33-72b6-412d-93b2-a05c4c2d4a5b;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 810c22f1-da1b-442a-88d3-7a5d91ccbcd9;
						}
					}
					{ IMessage 
						- _id = GUID fd2a6887-3ede-4b80-8123-2609cf303cf9;
						- _myState = 8192;
						- _name = "Add_notification";
						- _objectCreation = "321240116201721-4374123";
						- _umlDependencyID = "3160";
						- m_szSequence = "11.";
						- m_szActualArgs = "Info";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c43f7998-83ea-4e48-a116-140e2eec421d;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID a5089d90-fe00-4109-b376-cf136586d46c;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 90294c75-743b-4152-9965-e5ba9828b424;
						}
					}
					{ IMessage 
						- _id = GUID c836aa64-1ddc-43e1-bb5c-8f1bb699835e;
						- _name = "Update_notify_form";
						- _objectCreation = "321242116201721-4376123";
						- _umlDependencyID = "3419";
						- m_szSequence = "12.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c43f7998-83ea-4e48-a116-140e2eec421d;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
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
						- _id = GUID 57eb8258-0cd5-44b8-a61f-e4c169388f4d;
						- _name = "Update_notify_form";
						- _objectCreation = "321244116201721-4378123";
						- _umlDependencyID = "3423";
						- m_szSequence = "13.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 12cb1378-4ea7-4b4e-a1f4-409f94a3d5f6;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
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
						- _id = GUID 20e09dac-0090-41e5-8533-52ab800ccd60;
						- _name = "Log_in_user";
						- _objectCreation = "321246116201721-4380123";
						- _umlDependencyID = "2658";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3056f134-6b3f-4558-b4de-174dd9105b4a;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 24fb0545-4d6d-4b8d-832d-933da34a260e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Client.sbs";
							- _subsystem = "Client";
							- _class = "LoginForm";
							- _name = "Log_in_user()";
							- _id = GUID 0e26fb95-f04b-403a-903b-ff0e7b8a3978;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID e95c2fc6-1126-4c05-9dc9-6222b0dd3362;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 1e11dabd-0692-4aa0-9fc7-246e3310550e;
						}
					}
					{ IMessage 
						- _id = GUID a37e79e5-37c9-4bb1-a4b7-670056771d93;
						- _name = "Log_in_user";
						- _objectCreation = "321248116201721-4382123";
						- _umlDependencyID = "2662";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c43f7998-83ea-4e48-a116-140e2eec421d;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3056f134-6b3f-4558-b4de-174dd9105b4a;
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
							- _id = GUID 3f919efe-c384-4943-86db-c6138c4a1742;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID f6298112-f29e-4ba1-86da-7454590cded7;
						}
					}
					{ IMessage 
						- _id = GUID 3440f3fc-4cb9-4926-863b-a78d918ec89b;
						- _name = "Update_login_form";
						- _objectCreation = "321250116201721-4384123";
						- _umlDependencyID = "3289";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3056f134-6b3f-4558-b4de-174dd9105b4a;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c43f7998-83ea-4e48-a116-140e2eec421d;
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
						- _id = GUID 57bafc62-f7c1-4c6c-aa95-aa0e6584a936;
						- _name = "Show_actions_list";
						- _objectCreation = "321252116201721-4386123";
						- _umlDependencyID = "3323";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c43f7998-83ea-4e48-a116-140e2eec421d;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3056f134-6b3f-4558-b4de-174dd9105b4a;
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
							- _id = GUID 0d8a6ec0-734a-493e-94a2-b504c799be76;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 760c5971-67a8-4c22-a818-774f59abe174;
						}
					}
					{ IMessage 
						- _id = GUID 661bc253-75f4-4767-ae12-326e2c395ffe;
						- _name = "Show_actions_list";
						- _objectCreation = "321254116201721-4388123";
						- _umlDependencyID = "3327";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 8feff97b-2ede-41cd-a1dc-e026891207ae;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c43f7998-83ea-4e48-a116-140e2eec421d;
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
							- _id = GUID 4464fa2e-60ee-49cb-8738-175f14a341f2;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID e0c2de8f-3eef-4eb3-8555-102889305f76;
						}
					}
					{ IMessage 
						- _id = GUID ac9c03d3-913c-47f4-af85-bf0a73fa0b6f;
						- _name = "Open_actions_list_form";
						- _objectCreation = "321256116201721-4390123";
						- _umlDependencyID = "3838";
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 8feff97b-2ede-41cd-a1dc-e026891207ae;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 8feff97b-2ede-41cd-a1dc-e026891207ae;
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
							- _id = GUID 3973aaf4-68f3-4ed9-b21a-16eed7b6019e;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 18;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 76767779-9bcf-4770-8bb0-c9d527747fd5;
						- _objectCreation = "321258116201721-4392123";
						- _umlDependencyID = "1522";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 4b27784e-02ea-4c3d-96c3-ad5d7692b818;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 62;
					}
					{ IExecutionOccurrence 
						- _id = GUID 8a449a89-7b81-470d-a165-a098fdcb4068;
						- _objectCreation = "321260116201721-4394123";
						- _umlDependencyID = "1517";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 4b27784e-02ea-4c3d-96c3-ad5d7692b818;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 2c55b913-2f0e-43be-83ee-272ae07264ed;
						- _objectCreation = "321262116201721-4396123";
						- _umlDependencyID = "1521";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c1ce6645-9620-443e-9f13-906d3dfc5c89;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 141;
					}
					{ IExecutionOccurrence 
						- _id = GUID 4cae1fb0-d303-462d-890b-e0b729a36a8b;
						- _objectCreation = "321264116201721-4398123";
						- _umlDependencyID = "1525";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID c1ce6645-9620-443e-9f13-906d3dfc5c89;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID e0c1fe28-a23e-4cb1-9237-1d6d02f734eb;
						- _objectCreation = "321266116201721-4400123";
						- _umlDependencyID = "1511";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 74bf59c2-2df5-49b6-a544-5699753b3616;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 186;
					}
					{ IExecutionOccurrence 
						- _id = GUID dfb98b33-72b6-412d-93b2-a05c4c2d4a5b;
						- _objectCreation = "321268116201721-4402123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 6da9589e-d6fc-421b-bd99-c5d799289956;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 51;
					}
					{ IExecutionOccurrence 
						- _id = GUID 810c22f1-da1b-442a-88d3-7a5d91ccbcd9;
						- _objectCreation = "321270116201721-4404123";
						- _umlDependencyID = "1510";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 6da9589e-d6fc-421b-bd99-c5d799289956;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID a5089d90-fe00-4109-b376-cf136586d46c;
						- _objectCreation = "321272116201721-4406123";
						- _umlDependencyID = "1514";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID fd2a6887-3ede-4b80-8123-2609cf303cf9;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 90294c75-743b-4152-9965-e5ba9828b424;
						- _objectCreation = "321274116201721-4408123";
						- _umlDependencyID = "1518";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID fd2a6887-3ede-4b80-8123-2609cf303cf9;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 50;
					}
					{ IExecutionOccurrence 
						- _id = GUID 3f919efe-c384-4943-86db-c6138c4a1742;
						- _objectCreation = "321276116201721-4410123";
						- _umlDependencyID = "1513";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a37e79e5-37c9-4bb1-a4b7-670056771d93;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID f6298112-f29e-4ba1-86da-7454590cded7;
						- _objectCreation = "321278116201721-4412123";
						- _umlDependencyID = "1517";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID a37e79e5-37c9-4bb1-a4b7-670056771d93;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 117;
					}
					{ IExecutionOccurrence 
						- _id = GUID e95c2fc6-1126-4c05-9dc9-6222b0dd3362;
						- _objectCreation = "321280116201721-4414123";
						- _umlDependencyID = "1512";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 20e09dac-0090-41e5-8533-52ab800ccd60;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 1e11dabd-0692-4aa0-9fc7-246e3310550e;
						- _objectCreation = "321282116201721-4416123";
						- _umlDependencyID = "1516";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 20e09dac-0090-41e5-8533-52ab800ccd60;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 0d8a6ec0-734a-493e-94a2-b504c799be76;
						- _objectCreation = "321284116201721-4418123";
						- _umlDependencyID = "1520";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 57bafc62-f7c1-4c6c-aa95-aa0e6584a936;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 76;
					}
					{ IExecutionOccurrence 
						- _id = GUID 760c5971-67a8-4c22-a818-774f59abe174;
						- _objectCreation = "321286116201721-4420123";
						- _umlDependencyID = "1515";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 57bafc62-f7c1-4c6c-aa95-aa0e6584a936;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 4464fa2e-60ee-49cb-8738-175f14a341f2;
						- _objectCreation = "321288116201721-4422123";
						- _umlDependencyID = "1519";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 661bc253-75f4-4767-ae12-326e2c395ffe;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 40;
					}
					{ IExecutionOccurrence 
						- _id = GUID e0c2de8f-3eef-4eb3-8555-102889305f76;
						- _objectCreation = "321290116201721-4424123";
						- _umlDependencyID = "1514";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 661bc253-75f4-4767-ae12-326e2c395ffe;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 3973aaf4-68f3-4ed9-b21a-16eed7b6019e;
						- _objectCreation = "321292116201721-4426123";
						- _umlDependencyID = "1518";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID ac9c03d3-913c-47f4-af85-bf0a73fa0b6f;
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
			- _objectCreation = "321302116201721-4436123";
			- _umlDependencyID = "1932";
			- _lastModifiedTime = "12.11.2017::8:34:28";
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
				- elementList = 36;
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
					- m_transform = 0.194863 0 0 0.0662932 536.39 165.066 ;
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
					- m_transform = 0.194862 0 0 0.0662932 124.39 578.066 ;
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
				{ CGIAssociationEnd 
					- _id = GUID 26969f5b-5911-4539-a495-33a131f305ba;
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
						- _name = "its9. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \ò\å\ê\ó\ù\å\å \ð\à\ñ\ï\è\ñ\à\í\è\å \ç\à\í\ÿ\ò\è\é";
						- _id = GUID 8b90d8b4-2d95-4ae3-9613-7e3cef6fd0c3;
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
					- m_SourcePort = 310 1138 ;
					- m_TargetPort = 953 213 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "9. \Ï\ð\î\ñ\ì\î\ò\ð\å\ò\ü \ò\å\ê\ó\ù\å\å \ð\à\ñ\ï\è\ñ\à\í\è\å \ç\à\í\ÿ\ò\è\é";
						- _name = "its\Ï\ð\å\ï\î\ä\à\â\à\ò\å\ë\ü";
						- _id = GUID 8d77e721-bc97-487f-995d-1799dd061705;
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

