DROP DATABASE IF EXISTS DBPROJETO_INTEGRADOR;
CREATE DATABASE DBPROJETO_INTEGRADOR;
USE DBPROJETO_INTEGRADOR;

CREATE TABLE IMIGRANTE (
	IDIMIGRANTE INT NOT NULL AUTO_INCREMENT
    , NOME VARCHAR(120) NOT NULL
    , NACIONALIDADE VARCHAR(100) NOT NULL
    , DT_NASCIMENTO DATE NOT NULL
    , DOCUMENTO VARCHAR(50)
    , PRIMARY KEY (IDIMIGRANTE)
);

CREATE TABLE INFORMACAO (
	IDINFORMACAO INT NOT NULL AUTO_INCREMENT
	, IDIMIGRANTE INT NOT NULL 
    , TIPO VARCHAR(20) NOT NULL -- DEVE RECEBER APENAS (ESCOLARIDADE OU PROFISSIONAL)
    , DESCRICAO VARCHAR(120) NOT NULL
    , ANO_INICIO INT NOT NULL
    , ANO_TERMINO INT 
    , PRIMARY KEY (IDINFORMACAO)
    , FOREIGN KEY (IDIMIGRANTE) REFERENCES IMIGRANTE(IDIMIGRANTE)
);

CREATE TABLE SERVICO_APOIO (
	IDSERVICO_APOIO INT NOT NULL AUTO_INCREMENT
    , TIPO VARCHAR(50) NOT NULL -- DEVE RECEBER ALGO COMO (ONG, CENTRO DE ACOLHIMENTO, CURSO)
    , NOME VARCHAR(120) NOT NULL
    , ENDERECO VARCHAR(120) NOT NULL
    , TELEFONE VARCHAR(15)  NOT NULL
    , PRIMARY KEY (IDSERVICO_APOIO)
);

INSERT INTO IMIGRANTE (NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO) VALUES
('Aarav Sharma', 'Indiana', '1990-05-15', 'ABC12345'),
('Fatima Al-Jamil', 'Síria', '1988-09-22', 'SYR98765'),
('David Chen', 'Chinesa', '1995-02-10', 'CHN54321'),
('Maria Rodriguez', 'Venezuelana', '1992-11-30', 'VEN67890'),
('John Smith', 'Norte-americana', '1985-07-20', 'USA11223'),
('Olga Ivanova', 'Ucraniana', '1998-01-05', 'UKR44556'),
('Ahmed Khan', 'Paquistanesa', '1993-04-12', 'PAK77889'),
('Isabella Rossi', 'Italiana', '1991-08-18', 'ITA99001'),
('Mohammed Ali', 'Nigeriana', '1996-03-25', 'NGA22334'),
('Sophie Dubois', 'Francesa', '1989-12-08', 'FRA55667'),
('Carlos Gomez', 'Cubana', '1994-06-14', 'CUB88990'),
('Aisha Diallo', 'Senegalesa', '1999-10-01', 'SEN12121'),
('Kenji Tanaka', 'Japonesa', '1987-05-29', 'JPN34343'),
('Laura Schmidt', 'Alemã', '1990-09-03', 'DEU56565'),
('Andrés Morales', 'Colombiana', '1992-07-21', 'COL78787'),
('Yara da Silva', 'Angolana', '1997-02-17', 'AGO90909'),
('Liam Murphy', 'Irlandesa', '1986-11-11', 'IRL23232'),
('Sofia Petrova', 'Russa', '1995-08-07', 'RUS45454'),
('Omar Hassan', 'Egípcia', '1993-10-24', 'EGY67676'),
('Elena Popescu', 'Romana', '1991-04-09', 'ROU89898');

INSERT INTO INFORMACAO (IDIMIGRANTE, TIPO, DESCRICAO, ANO_INICIO, ANO_TERMINO) VALUES
(1, 'PROFISSIONAL', 'Engenheiro de Software', 2013, 2023),
(1, 'ESCOLARIDADE', 'Bacharelado em Ciência da Computação', 2009, 2013),
(2, 'PROFISSIONAL', 'Médica', 2015, 2022),
(3, 'ESCOLARIDADE', 'Ensino Médio Completo', 2011, 2014),
(4, 'PROFISSIONAL', 'Jornalista', 2016, 2023),
(5, 'PROFISSIONAL', 'Professor de Inglês', 2010, 2021),
(6, 'ESCOLARIDADE', 'Mestrado em Relações Internacionais', 2019, 2021),
(7, 'PROFISSIONAL', 'Técnico de Enfermagem', 2018, 2023),
(8, 'PROFISSIONAL', 'Chef de Cozinha', 2014, 2022),
(9, 'ESCOLARIDADE', 'Ensino Fundamental Completo', 2005, 2013),
(10, 'PROFISSIONAL', 'Designer Gráfico', 2012, 2023),
(11, 'PROFISSIONAL', 'Mecânico de Automóveis', 2015, 2023),
(12, 'ESCOLARIDADE', 'Bacharelado em Administração', 2017, 2021),
(13, 'PROFISSIONAL', 'Analista de Sistemas', 2010, 2022),
(14, 'ESCOLARIDADE', 'Doutorado em Engenharia Química', 2016, 2020),
(15, 'PROFISSIONAL', 'Advogado', 2017, 2023),
(16, 'PROFISSIONAL', 'Eletricista', 2019, 2023),
(17, 'ESCOLARIDADE', 'Curso Técnico em Edificações', 2010, 2012),
(18, 'PROFISSIONAL', 'Tradutora', 2018, 2023),
(20, 'ESCOLARIDADE', 'Graduação em Letras', 2010, 2014);

INSERT INTO SERVICO_APOIO (TIPO, NOME, ENDERECO, TELEFONE) VALUES
('ONG', 'Caritas Brasileira', 'Rua da Consolação, 123, São Paulo', '(11) 3333-4444'),
('CENTRO DE ACOLHIMENTO', 'Casa do Imigrante', 'Av. das Nações, 456, Rio de Janeiro', '(21) 98765-4321'),
('CURSO', 'Português para Estrangeiros - Aulas Abertas', 'Rua Sete de Setembro, 789, Belo Horizonte', '(31) 3210-9876'),
('ONG', 'Missão Paz', 'Praça da Sé, 1, São Paulo', '(11) 2222-5555'),
('CENTRO DE ACOLHIMENTO', 'Centro de Referência do Imigrante', 'Rua do Ouvidor, 10, Curitiba', '(41) 3030-4040'),
('CURSO', 'Capacitação Profissional para Refugiados', 'Av. Ipiranga, 200, Porto Alegre', '(51) 9999-8888'),
('ONG', 'Médicos Sem Fronteiras Brasil', 'Rua da Glória, 300, Rio de Janeiro', '(21) 2121-3131'),
('CENTRO DE ACOLHIMENTO', 'Arsenal da Esperança', 'Rua Dr. Almeida Lima, 900, São Paulo', '(11) 2291-0944'),
('CURSO', 'Informática Básica para Imigrantes', 'Rua Augusta, 50, Salvador', '(71) 3434-5656'),
('ONG', 'ACNUR Brasil', 'Setor de Embaixadas Norte, 801, Brasília', '(61) 3044-5744'),
('CENTRO DE ACOLHIMENTO', 'Pastoral do Migrante', 'Av. Tiradentes, 676, São Paulo', '(11) 3311-7644'),
('CURSO', 'Culinária Brasileira para Imigrantes', 'Rua do Lavradio, 100, Rio de Janeiro', '(21) 98877-6655'),
('ONG', 'Compassiva', 'Rua Teodoro Sampaio, 45, São Paulo', '(11) 4321-8765'),
('CENTRO DE ACOLHIMENTO', 'Aldeias Infantis SOS Brasil', 'Rua das Acácias, 15, Recife', '(81) 3113-2112'),
('CURSO', 'Preparatório para Revalidação de Diploma', 'Av. Paulista, 900, São Paulo', '(11) 97654-3210'),
('ONG', 'IKMR - Eu Conheço Meus Direitos', 'Rua Barão de Itapetininga, 255, São Paulo', '(11) 3255-0629'),
('CENTRO DE ACOLHIMENTO', 'Cáritas Arquidiocesana do Rio de Janeiro', 'Rua São Francisco Xavier, 483, Rio de Janeiro', '(21) 2567-4282'),
('CURSO', 'Empreendedorismo para Imigrantes', 'Rua 25 de Março, 1000, São Paulo', '(11) 98888-7777'),
('ONG', 'Visão Mundial', 'SHIS QI 09, Bloco A, Brasília', '(61) 3367-1011'),
('CENTRO DE ACOLHIMENTO', 'CAMI - Centro de Apoio e Pastoral do Migrante', 'Alameda Nothmann, 485, São Paulo', '(11) 3333-0561');

SELECT * FROM IMIGRANTE;