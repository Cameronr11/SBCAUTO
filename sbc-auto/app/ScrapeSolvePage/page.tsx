"use client";
import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Spinner, useToast } from '@chakra-ui/react';


//connected to scraping backend endpoint in app.py
const ScrapeSolvePage = () => {
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();
  const toast = useToast();

  const handleScrapePlayers = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:5000/scrape', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
      });
      const data = await response.json();
      if (response.ok) {
        toast({
          title: 'Scraping Complete',
          description: data.message,
          status: 'success',
          duration: 5000,
          isClosable: true,
        });
      } else {
        toast({
          title: 'Error',
          description: data.message,
          status: 'error',
          duration: 5000,
          isClosable: true,
        });
      }
    } catch (error) {
      toast({
        title: 'Error',
        description: 'An error occurred while scraping.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    } finally {
      setIsLoading(false);
    }
  };

  const navigateToSbcSolver = () => {
    router.push('/SolverPage'); // Update with your actual path
  };

  return (
    <div className="flex h-screen">
      <div className="flex-1 flex flex-col items-center justify-center bg-black text-white">
        <h2>Step 1: Gather Available Players</h2>
        <button
          onClick={handleScrapePlayers}
          className="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded flex items-center justify-center"
          disabled={isLoading}
        >
          {isLoading ? <Spinner size="md" color="white" /> : 'Start Gathering'}
        </button>
        <p className="mt-2">Relax, this may take a minute or two.</p>
      </div>
      <div className="flex-1 flex flex-col items-center justify-center bg-gray-800 text-white">
        <h2>Step 2: Travel to SBC Solver</h2>
        <button
          onClick={navigateToSbcSolver}
          className="mt-4 bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
        >
          Go to Solver
        </button>
      </div>
    </div>
  );
};

export default ScrapeSolvePage;

