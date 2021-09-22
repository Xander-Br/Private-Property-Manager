-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Dim 13 Juin 2021 à 19:00
-- Version du serveur :  5.6.20-log
-- Version de PHP :  5.4.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `breuil_alexandre_info1b_private_property_manager_104`
--

-- --------------------------------------------------------

DROP DATABASE IF EXISTS breuil_alexandre_info1b_private_property_manager_104;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS breuil_alexandre_info1b_private_property_manager_104;

-- Utilisation de cette base de donnée

USE breuil_alexandre_info1b_private_property_manager_104;

--
-- Structure de la table `t_owner`
--

CREATE TABLE IF NOT EXISTS `t_owner` (
`O_ID` int(11) NOT NULL,
  `O_F_Name` varchar(100) NOT NULL,
  `O_L_Name` varchar(100) NOT NULL,
  `O_Email` varchar(100) NOT NULL,
  `O_ContactNumber` varchar(100) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=38 ;

--
-- Contenu de la table `t_owner`
--

INSERT INTO `t_owner` (`O_ID`, `O_F_Name`, `O_L_Name`, `O_Email`, `O_ContactNumber`) VALUES
(35, 'Alexandre', 'Breuil', 'breuilalexandre2003@gmail.com', '0797425409'),
(36, 'Tiago', 'Amaro', 'tiago.amaro@gmail.com', '0732145676'),
(37, 'Nathan', 'Demierre', 'nathan.demierre@gmail.com', '0323213214');

-- --------------------------------------------------------

--
-- Structure de la table `t_owner_property`
--

CREATE TABLE IF NOT EXISTS `t_owner_property` (
`OP_ID` int(11) NOT NULL,
  `FK_O_ID` int(11) NOT NULL,
  `FK_P_ID` int(11) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=28 ;

--
-- Contenu de la table `t_owner_property`
--

INSERT INTO `t_owner_property` (`OP_ID`, `FK_O_ID`, `FK_P_ID`) VALUES
(25, 35, 8),
(26, 36, 9),
(27, 37, 1);

-- --------------------------------------------------------

--
-- Structure de la table `t_property`
--

CREATE TABLE IF NOT EXISTS `t_property` (
`P_ID` int(11) NOT NULL,
  `P_Name` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `P_Price` float NOT NULL,
  `P_Description` varchar(500) NOT NULL,
  `P_Type` varchar(100) NOT NULL,
  `P_Construction_Year` date NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=10 ;

--
-- Contenu de la table `t_property`
--

INSERT INTO `t_property` (`P_ID`, `P_Name`, `P_Price`, `P_Description`, `P_Type`, `P_Construction_Year`) VALUES
(1, 'Maison de Maccaud', 1500000, 'Une belle maison de merde', 'Maison', '2021-06-07'),
(8, 'Une maison super bien', 2000000, 'La maison du développeur de cette magnifique application', 'Maison xxxxxl', '2021-06-22'),
(9, 'Appartement 2.5 piéces', 300000, 'Appartement, 2.5 piéces, vu sur le lac et les montagnes', 'Appartement', '2016-10-17');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_owner`
--
ALTER TABLE `t_owner`
 ADD PRIMARY KEY (`O_ID`);

--
-- Index pour la table `t_owner_property`
--
ALTER TABLE `t_owner_property`
 ADD PRIMARY KEY (`OP_ID`), ADD KEY `FK_O_ID` (`FK_O_ID`), ADD KEY `FK_P_ID` (`FK_P_ID`);

--
-- Index pour la table `t_property`
--
ALTER TABLE `t_property`
 ADD PRIMARY KEY (`P_ID`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_owner`
--
ALTER TABLE `t_owner`
MODIFY `O_ID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=38;
--
-- AUTO_INCREMENT pour la table `t_owner_property`
--
ALTER TABLE `t_owner_property`
MODIFY `OP_ID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT pour la table `t_property`
--
ALTER TABLE `t_property`
MODIFY `P_ID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=10;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `t_owner_property`
--
ALTER TABLE `t_owner_property`
ADD CONSTRAINT `t_owner_property_ibfk_1` FOREIGN KEY (`FK_O_ID`) REFERENCES `t_owner` (`O_ID`),
ADD CONSTRAINT `t_owner_property_ibfk_2` FOREIGN KEY (`FK_P_ID`) REFERENCES `t_property` (`P_ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
