-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 03:35 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online_ticket_bus`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_detail`
--

CREATE TABLE `user_detail` (
  `Name` varchar(30) NOT NULL,
  `Phone_number` varchar(10) NOT NULL,
  `Destination` varchar(20) NOT NULL,
  `Date` varchar(10) NOT NULL,
  `Quantity_ticket` int(1) NOT NULL,
  `Total_price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_detail`
--

INSERT INTO `user_detail` (`Name`, `Phone_number`, `Destination`, `Date`, `Quantity_ticket`, `Total_price`) VALUES
('syahirah', '0145292456', 'Kedah to Pahang', '12/5/24', 3, 180.9),
('lee do hyun', '0175292456', 'Kedah to Pahang', '2/15/24', 3, 180.9),
('jennie', '0115292456', 'Kedah to Pahang', '3/7/24', 2, 134),
('kylie', '0185292259', 'Kedah to Terengganu', '3/7/24', 1, 75),
('izzati ', '0165347654', 'Kedah to Terengganu', '1/1/24', 1, 75),
('syafiqah', '0128976542', 'Kedah to Terengganu', '1/10/24', 1, 75),
('mark', '0176534256', 'Kedah to Pahang', '2/29/24', 3, 180.9);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
