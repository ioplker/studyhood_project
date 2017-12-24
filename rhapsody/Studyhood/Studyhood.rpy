I-Logix-RPY-Archive version 8.8.0 C# 6107223
{ IProject 
	- _id = GUID 3e01fd52-d67b-4ddb-94c1-872a5f8b094c;
	- _myState = 8192;
	- _name = "Studyhood";
	- codeUpdateCGTime = 12.24.2017::11:8:51;
	- Dependencies = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDependency 
			- _id = GUID 6c7dc46b-a7a2-452d-a116-45bed89c844a;
			- _myState = 2048;
			- _name = "CodeCentricCSharp";
			- codeUpdateCGTime = 12.24.2017::11:5:43;
			- Stereotypes = { IRPYRawContainer 
				- size = 1;
				- value = 
				{ IHandle 
					- _m2Class = "IStereotype";
					- _filename = "PredefinedTypes.sbs";
					- _subsystem = "PredefinedTypes";
					- _class = "";
					- _name = "AppliedProfile";
					- _id = GUID d2eca2c1-e5a5-4296-9453-29283c4ed8bc;
				}
			}
			- _modifiedTimeWeak = 12.24.2017::11:5:43;
			- _dependsOn = { INObjectHandle 
				- _m2Class = "IProfile";
				- _filename = "$OMROOT\\Settings\\CodeCentric\\CodeCentric752CSharp.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "CodeCentricCSharp";
				- _id = GUID 81d7329b-ad5c-415c-bd03-686696a55532;
			}
		}
	}
	- _modifiedTimeWeak = 12.24.2017::12:47:6;
	- _theMainDiagram = { IHandle 
		- _m2Class = "IDiagram";
		- _id = GUID 85dc7942-8762-4d52-8586-9d3f2f95bf45;
	}
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
		- _id = GUID e562a913-07c1-41a6-9d92-153ccc244bf4;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "Studyhood.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "Studyhood";
		- _id = GUID f174d8f9-4705-4935-bcd5-5fb30d7bd30b;
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
		- size = 4;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID e562a913-07c1-41a6-9d92-153ccc244bf4;
		}
		{ ISubsystem 
			- fileName = "Studyhood";
			- _id = GUID b390e90b-ecbf-424e-984d-18d578aa56fb;
		}
		{ IProfile 
			- fileName = "CodeCentric752CSharp";
			- _persistAs = "$OMROOT\\Settings\\CodeCentric";
			- _id = GUID 81d7329b-ad5c-415c-bd03-686696a55532;
			- _name = "CodeCentricCSharp";
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "CSharpProfile";
			- _persistAs = "$OMROOT\\Profiles\\CSharp\\";
			- _id = GUID 25d37c62-0a81-48f9-852f-75e181c43db0;
			- _name = "C#";
			- _isReference = 1;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ IDiagram 
			- _id = GUID ce7193f6-33f0-4352-bf56-e759106b004e;
			- _myState = 8192;
			- _name = "Model1";
			- Stereotypes = { IRPYRawContainer 
				- size = 1;
				- value = 
				{ IHandle 
					- _m2Class = "IStereotype";
					- _filename = "$OMROOT\\Profiles\\CSharp\\\\CSharpProfile.sbs";
					- _subsystem = "C#";
					- _class = "";
					- _name = "c# Class Diagram";
					- _id = GUID 0b10f104-d1b7-401c-bae3-38d06d8fd00b;
				}
			}
			- _modifiedTimeWeak = 1.1.1970::7:0:0;
			- _lastModifiedTime = "12.24.2017::11:5:46";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 74fd89e4-98af-49a3-902c-cb209e07ecf6;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID ce7193f6-33f0-4352-bf56-e759106b004e;
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
				- elementList = 1;
				{ CGIClass 
					- _id = GUID a118a2e5-17c2-40cb-99b8-50a18852a30c;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID a7b6488b-519e-44c0-861a-972dd4105046;
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
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID a118a2e5-17c2-40cb-99b8-50a18852a30c;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID e562a913-07c1-41a6-9d92-153ccc244bf4;
			}
		}
		{ IDiagram 
			- _id = GUID 85dc7942-8762-4d52-8586-9d3f2f95bf45;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
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
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
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
						- _Name = "ObjectModelGe";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "AutoPopulate";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "EnabledOnUpdateModel";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "ModelOverviewStudyhood";
			- _modifiedTimeWeak = 1.1.1970::7:0:0;
			- _lastModifiedTime = "12.24.2017::12:47:6";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 7e9245a5-3ffd-495c-a5fa-11c32dfef1c6;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 85dc7942-8762-4d52-8586-9d3f2f95bf45;
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
				- elementList = 3;
				{ CGIClass 
					- _id = GUID c3946b64-43ee-491d-83fc-c8e8a73a2c02;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID a7b6488b-519e-44c0-861a-972dd4105046;
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
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIPackage 
					- _id = GUID 9bcb1ffa-cbee-497f-a9fd-0406f35519d8;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Studyhood.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Studyhood";
						- _id = GUID b390e90b-ecbf-424e-984d-18d578aa56fb;
					}
					- m_pParent = GUID c3946b64-43ee-491d-83fc-c8e8a73a2c02;
					- m_name = { CGIText 
						- m_str = "Studyhood";
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
					- m_transform = 0.0986842 0 0 0.0556038 40 40 ;
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
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIPackage 
					- _id = GUID f9b93d16-c7c9-4299-b15c-9bd224167359;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Studyhood.sbs";
						- _subsystem = "Studyhood::Studyhood";
						- _class = "";
						- _name = "server";
						- _id = GUID fdc1714a-58df-4a2c-b41b-4b666011f641;
					}
					- m_pParent = GUID c3946b64-43ee-491d-83fc-c8e8a73a2c02;
					- m_name = { CGIText 
						- m_str = "server";
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
					- m_transform = 0.0986842 0 0 0.0556038 248 40 ;
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
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID c3946b64-43ee-491d-83fc-c8e8a73a2c02;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID e562a913-07c1-41a6-9d92-153ccc244bf4;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID 5e775f7a-e735-44d5-9cd3-5c07513f37af;
		}
		{ IComponent 
			- fileName = "Studyhood";
			- _id = GUID f174d8f9-4705-4935-bcd5-5fb30d7bd30b;
		}
	}
}

