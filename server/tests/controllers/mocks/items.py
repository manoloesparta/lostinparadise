VALID_REQUEST = {"query": "cargador"}

INVALID_REQUEST = {}

LOST_ITEMS_MOCK = [
    {
        "buildingName": "Edificio de Posgrado",
        "category": "Electrónico",
        "description": "Cargador HP 7202",
        "foundBy": "CORTES SANTIAGO, ALFREDO",
        "foundOn": "2020-02-20",
        "receivedBy": "Fernando Cordero",
        "receivedObservations": "Pendiente",
        "roomNumber": 7302,
        "searchString": "electronico cargador hp 7202",
        "status": "Reportado",
        "uuid": "f2ac546a-82a5-438e-80b7-a9724d560076",
    },
    {
        "buildingName": "Edificio de Aulas de Profesional E1",
        "category": "Cómputo",
        "description": "spectre 1206 marco zuñiga",
        "foundBy": "JUAN CARLOS PALOMARES",
        "foundOn": "2020-02-20",
        "receivedBy": "Alonso Hernandez Pardo",
        "receivedObservations": "Pendiente",
        "roomNumber": 1205,
        "searchString": "computo spectre 1206 marco zuniga",
        "status": "Reportado",
        "uuid": "c67100d4-1d6b-482b-a386-2a8afcdc1802",
    },
    {
        "buildingName": "Edificio de Aulas de Profesional E1",
        "category": "Electrónico",
        "description": "Cargador Iphone Blanco USB Salón 1303,",
        "foundBy": "JUAN CARLOS PALOMARES",
        "foundOn": "2020-02-20",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 1303,
        "searchString": "electronico cargador iphone blanco usb salon 1303,",
        "status": "Reportado",
        "uuid": "81691b6f-1e6f-4025-b075-dd056686dbc9",
    },
    {
        "buildingName": "Edificio de Posgrado",
        "category": "Electrónico",
        "description": "Cargador HP punta AZUL Salón  7301, miércoles 19",
        "foundBy": "ARCOS DIAZ, ROBERTO",
        "foundOn": "2020-02-20",
        "receivedBy": "Christopher Medina",
        "receivedObservations": "Pendiente",
        "roomNumber": 7301,
        "searchString": "electronico cargador hp punta azul salon  7301, miercoles "
        "19",
        "status": "Reportado",
        "uuid": "9c4ed0fc-5869-4966-92e2-df6901720e93",
    },
    {
        "buildingName": "Edificio de Aulas 4000",
        "category": "Cómputo",
        "description": "cargador hp 4204",
        "foundBy": "CABRERA , ALVARO",
        "foundOn": "2020-02-20",
        "receivedBy": "Alonso Hernandez Pardo",
        "receivedObservations": "Pendiente",
        "roomNumber": 4204,
        "searchString": "computo cargador hp 4204",
        "status": "Reportado",
        "uuid": "87e302cf-3cb8-4811-aff1-af9a24d567fd",
    },
    {
        "buildingName": "Edificio de Posgrado",
        "category": "Electrónico",
        "description": "Cargador MAC 7308 SABADO 22/02/20",
        "foundBy": "FERNANDO CORDERO",
        "foundOn": "2020-02-24",
        "receivedBy": "Fernando Cordero",
        "receivedObservations": "Pendiente",
        "roomNumber": 7308,
        "searchString": "electronico cargador mac 7308 sabado 22/02/20",
        "status": "Reportado",
        "uuid": "4004a5d5-a284-496f-ad53-ca5dc6c2a6e3",
    },
    {
        "buildingName": "Aulas 9000",
        "category": "Electrónico",
        "description": "Cargador Iphone Salón 9102,",
        "foundBy": "JUAN CARLOS PALOMARES",
        "foundOn": "2020-02-26",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 9102,
        "searchString": "electronico cargador iphone salon 9102,",
        "status": "Reportado",
        "uuid": "3c5a64a9-28db-4c98-8413-b9e0171fe375",
    },
    {
        "buildingName": "Edificio de Aulas 4000",
        "category": "Electrónico",
        "description": "Cargador Apple USB Blanco entrada C, Salón 4306",
        "foundBy": "ARMENDARIZ PARDO, TANIA       ",
        "foundOn": "2020-02-27",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 4306,
        "searchString": "electronico cargador apple usb blanco entrada c, salon "
        "4306",
        "status": "Reportado",
        "uuid": "4eacb07d-d160-463f-9a38-c3504995c447",
    },
    {
        "buildingName": "Edificio de Aulas de Profesional E1",
        "category": "Electrónico",
        "description": "Cargador Iphone USB  Blanco   Salón 1306, ",
        "foundBy": "JUAN CARLOS PALOMARES",
        "foundOn": "2020-03-02",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 1306,
        "searchString": "electronico cargador iphone usb  blanco   salon 1306, ",
        "status": "Reportado",
        "uuid": "f5dc6419-4833-4705-ab0b-fa4f2ad8a683",
    },
    {
        "buildingName": "Edificio de Aulas de Profesional E1",
        "category": "Electrónico",
        "description": "Cargador Android Negro Salón 1204,",
        "foundBy": "JUAN CARLOS PALOMARES",
        "foundOn": "2020-03-05",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 1204,
        "searchString": "electronico cargador android negro salon 1204,",
        "status": "Reportado",
        "uuid": "3d73d0e9-6100-42dd-9f0f-1e347b9c9439",
    },
    {
        "buildingName": "Aulas 9000",
        "category": "Electrónico",
        "description": "Cargador mACKBOOK   USB Salón 9104,",
        "foundBy": "CABRERA , ALVARO",
        "foundOn": "2020-03-05",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 9104,
        "searchString": "electronico cargador mackbook   usb salon 9104,",
        "status": "Reportado",
        "uuid": "37a1569a-18fd-4d1c-9949-2f0af559e00b",
    },
    {
        "buildingName": "Edificio de Aulas de Profesional E1",
        "category": "Accesorios Personales",
        "description": "cargador iphone 1302",
        "foundBy": "MIGUEL ALONSO HERNANDEZ",
        "foundOn": "2020-03-11",
        "receivedBy": "Alonso Hernandez Pardo",
        "receivedObservations": "Pendiente",
        "roomNumber": 1302,
        "searchString": "accesorios personales cargador iphone 1302",
        "status": "Reportado",
        "uuid": "14483b5f-5282-4b68-bbc2-cd6968060322",
    },
    {
        "buildingName": "Aulas 9000",
        "category": "Electrónico",
        "description": "Laptop HP GRIS Salón 9103,",
        "foundBy": "RAYON ORTIZ, MARCO ANTONIO",
        "foundOn": "2020-03-13",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 9106,
        "searchString": "electronico laptop hp gris salon 9103,",
        "status": "Reportado",
        "uuid": "b16f3d44-2697-44ab-ba67-f5065a5296f5",
    },
    {
        "buildingName": "Aulas 9000",
        "category": "Electrónico",
        "description": "Laptop HP gris Salón 9103",
        "foundBy": "RAYON ORTIZ, MARCO ANTONIO",
        "foundOn": "2020-03-13",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 9103,
        "searchString": "electronico laptop hp gris salon 9103",
        "status": "Reportado",
        "uuid": "083addd4-26be-462a-8abc-2a64b1e811c3",
    },
    {
        "buildingName": "Aulas 9000",
        "category": "Electrónico",
        "description": "Cargador HP Punta Chica Azul, Salón 9101,",
        "foundBy": "CABRERA , ALVARO",
        "foundOn": "2020-03-13",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 9101,
        "searchString": "electronico cargador hp punta chica azul, salon 9101,",
        "status": "Reportado",
        "uuid": "23672a82-bf98-4924-9df9-9cfbc1b4b97c",
    },
    {
        "buildingName": "Edificio de Aulas de Profesional E1",
        "category": "Cómputo",
        "claimedBy": "QUINTERO NAVARRO, SOFIA       ",
        "deliveredAt": "Tecnología educativa",
        "deliveredBy": "Joel Lozano ",
        "deliveredObservations": "Pendiente",
        "deliveredOn": "2019-09-10",
        "description": "laptop lenovo negra-gris 1204",
        "foundBy": "MEDINA FLORES, CHRISTOPHER PAUL",
        "foundOn": "2019-09-10",
        "receivedBy": "Christopher Medina",
        "receivedObservations": "Pendiente",
        "roomNumber": 1204,
        "searchString": "computo laptop lenovo negra-gris 1204",
        "status": "Entregado",
        "uuid": "7753caaa-c046-4cf1-98a9-b01baedd3b10",
    },
    {
        "buildingName": "Edificio de Aulas de Profesional E1",
        "category": "Electrónico",
        "claimedBy": "QUINTERO NAVARRO, SOFIA       ",
        "deliveredAt": "Tecnología Educativa",
        "deliveredBy": "Alonso Hernandez Pardo",
        "deliveredObservations": "Pendiente",
        "deliveredOn": "2019-11-19",
        "description": "Cargador iphone usb salon 1205,",
        "foundBy": "JUAN CARLOS PALOMARES",
        "foundOn": "2019-11-15",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 1205,
        "searchString": "electronico cargador iphone usb salon 1205,",
        "status": "Entregado",
        "uuid": "84af3d02-9a49-4a85-81f3-2129505903b8",
    },
    {
        "buildingName": "Edificio de Aulas de Preparatoria E2",
        "category": "Electrónico",
        "claimedBy": "RAMIREZ ALCARAZ, RENE         ",
        "deliveredAt": "Tecnología Educativa",
        "deliveredBy": "Fernando Cordero",
        "deliveredObservations": "Pendiente",
        "deliveredOn": "2020-01-28",
        "description": "Cargador usb cable negro iphone salón 2306,",
        "foundBy": "CABRERA , ALVARO",
        "foundOn": "2020-01-20",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 2306,
        "searchString": "electronico cargador usb cable negro iphone salon 2306,",
        "status": "Entregado",
        "uuid": "2b80e41b-fbfc-49d4-8947-179419f206f6",
    },
    {
        "buildingName": "Edificio de Aulas de Profesional E1",
        "category": "Electrónico",
        "claimedBy": "RAMIREZ HERRERA, ZITLALI      ",
        "deliveredAt": "Tecnología educativa",
        "deliveredBy": "Jose Alfredo Ulloa Valdéz",
        "deliveredObservations": "Pendiente",
        "deliveredOn": "2019-10-17",
        "description": "cargador macsafe 2 1302",
        "foundBy": "MACIAS BARRAZA, INES VERONICA",
        "foundOn": "2019-10-10",
        "receivedBy": "Alonso Hernandez Pardo",
        "receivedObservations": "Pendiente",
        "roomNumber": 1302,
        "searchString": "electronico cargador macsafe 2 1302",
        "status": "Entregado",
        "uuid": "28d43c04-0d5a-473e-9a3d-6067747f875a",
    },
    {
        "buildingName": "Aulas 9000",
        "category": "Electrónico",
        "claimedBy": "RAMOS JIMENEZ MADRIGAL MOISES ",
        "deliveredAt": "Tecnología Educativa",
        "deliveredBy": "Alonso Hernandez Pardo",
        "deliveredObservations": "Pendiente",
        "deliveredOn": "2019-11-26",
        "description": "Cargador MAC 9107",
        "foundBy": "CHAVEZ CARRAZCO, CRISTIAN     ",
        "foundOn": "2019-11-25",
        "receivedBy": "Fernando Cordero",
        "receivedObservations": "Pendiente",
        "roomNumber": 9107,
        "searchString": "electronico cargador mac 9107",
        "status": "Entregado",
        "uuid": "3aa79df0-80ef-442e-8053-64228acf4584",
    },
    {
        "buildingName": "Aulas 9000",
        "category": "Electrónico",
        "claimedBy": "RAMOS NICOLAU, MARIA          ",
        "deliveredAt": "Tecnología Educativa",
        "deliveredBy": "Christopher Medina",
        "deliveredObservations": "Pendiente",
        "deliveredOn": "2019-10-15",
        "description": "Cargador Iphone Blanco  Salón 9101, ",
        "foundBy": "RAYON ORTIZ, MARCO ANTONIO",
        "foundOn": "2019-10-14",
        "receivedBy": "Joel Lozano ",
        "receivedObservations": "Pendiente",
        "roomNumber": 9102,
        "searchString": "electronico cargador iphone blanco  salon 9101, ",
        "status": "Entregado",
        "uuid": "962fe76c-88cb-493b-ac21-d8a09bd6fc39",
    },
    {
        "buildingName": "Aulas 3000",
        "category": "Electrónico",
        "claimedBy": "RENDON IRIBE, RENE            ",
        "deliveredAt": "Tecnología Educativa",
        "deliveredBy": "Fernando Cordero",
        "deliveredObservations": "Pendiente",
        "deliveredOn": "2020-02-12",
        "description": "Cargador Samsung 3102",
        "foundBy": "CARLOS CRUZ RESENDEZ",
        "foundOn": "2020-02-11",
        "receivedBy": "Fernando Cordero",
        "receivedObservations": "Pendiente",
        "roomNumber": 3102,
        "searchString": "electronico cargador samsung 3102",
        "status": "Entregado",
        "uuid": "959255d0-ef1f-467f-9c87-7aaf3af2a92a",
    },
]
