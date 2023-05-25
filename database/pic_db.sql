-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2023 at 09:53 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pic_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `pic_tb`
--

CREATE TABLE `pic_tb` (
  `ID` int(11) NOT NULL,
  `description` text NOT NULL,
  `image_path` varchar(256) NOT NULL,
  `name` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pic_tb`
--

INSERT INTO `pic_tb` (`ID`, `description`, `image_path`, `name`, `position`, `country`) VALUES
(1, 'First Black USA President', 'C:\\Users\\hp\\Desktop\\VoiceToImageRecSys\\images\\President_Barack_Obama.jpg', 'Obama', 'Former USA President', 'USA'),
(3, 'BCC Rector', 'C:\\Users\\hp\\Desktop\\VoiceToImageRecSys\\images\\sujith.jpeg', 'Sujith', 'Rector', 'India'),
(4, 'Chinese', 'C:\\Users\\hp\\Desktop\\VoiceToImageRecSys\\images\\president of china.jpg', 'jin', 'President of China', 'China'),
(5, 'USA President', 'C:\\Users\\hp\\Desktop\\VoiceToImageRecSys\\images\\Joe_Biden_presidential_portrait.jpg', 'Joe Biden', 'President of the USA', 'America');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pic_tb`
--
ALTER TABLE `pic_tb`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pic_tb`
--
ALTER TABLE `pic_tb`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
