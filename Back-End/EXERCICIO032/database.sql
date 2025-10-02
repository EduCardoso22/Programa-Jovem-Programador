DROP DATABASE IF EXISTS controle_gastos
CREATE DATABASE controle_gastos;
USE controle_gastos;

CREATE TABLE IF NOT EXISTS GASTO (
  `IDGASTO` INT NOT NULL AUTO_INCREMENT,
  `DESCRICAO` VARCHAR(255) NOT NULL,
  `CATEGORIA` VARCHAR(100) NOT NULL COMMENT 'Categorias pré-definidas: Educacao, Alimentacao, Transporte, Lazer.',
  `VALOR` DECIMAL(10,2) NOT NULL,
  `DT_GASTO` DATE NOT NULL,
  PRIMARY KEY (`IDGASTO`)
);

INSERT INTO GASTO (DESCRICAO, CATEGORIA, VALOR, DT_GASTO) VALUES
('Curso de Python', 'Educacao', 199.00, '2025-02-19'),
('Palestra de IA', 'Educacao', 30.00, '2025-02-19'),
('Almoço Restaurante', 'Alimentacao', 29.00, '2025-02-19'),
('Uber para o trabalho', 'Transporte', 14.00, '2025-02-19'),
('Uber para casa', 'Transporte', 9.00, '2025-02-19'),
('Ingresso Cinema', 'Lazer', 39.00, '2025-02-19');