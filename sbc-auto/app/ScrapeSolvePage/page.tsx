"use client";
import React, { useState, useEffect, useRef } from 'react';
import { useRouter } from 'next/navigation';
import { Spinner, useToast, Input, Button as ChakraButton, Box, Text, Button } from '@chakra-ui/react';
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

const ScrapeSolvePage = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [is2FARequired, setIs2FARequired] = useState(false);
  const [twoFACode, setTwoFACode] = useState('');
  const router = useRouter();
  const toast = useToast();
  const [progress, setProgress] = useState(0);
  const totalPlayersRef = useRef(1); // Use a ref to keep track of the total players
  const [totalPlayers, setTotalPlayers] = useState(1); // You might still keep this if you need to trigger re-renders


  useEffect(() => {
    socket.on('num_players', ({ num_players }) => {
      console.log('event happened to set num players');
      console.log(`Total players to scrape: ${num_players}`);
      totalPlayersRef.current = num_players; // Update ref value
      setTotalPlayers(num_players); // Update state if needed for re-render
      setProgress(0); // Reset progress on new scrape operation
    });

    socket.on('scraped_players', ({ scraped_players }) => {
      console.log(`Scraped players so far: ${scraped_players}`);
      // Use the current value from the ref
      console.log(`Total players to scrape: ${totalPlayersRef.current}`)
      const updatedProgress = Math.round((scraped_players / totalPlayersRef.current) * 1000)/10;
      console.log(`Updated progress: ${updatedProgress}%`);
      setProgress(updatedProgress);
    });

    return () => {
      socket.off('num_players');
      socket.off('scraped_players');
    };
  }, []);   
  
  const handleScrapePlayers = async (): Promise<void> => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:5000/scrape', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
      });
      const data = await response.json();
      if (response.ok) {
        if (data.status === '2FA Required') {
          setIs2FARequired(true);
          toast({
            title: '2FA Verification Needed',
            description: data.message,
            status: 'info',
            duration: 5000,
            isClosable: true,
          });
        } else {
          showSuccessAndNavigate();
        }
      } else {
        showError(data.message);
      }
    } catch (error) {
      showError('An error occurred while scraping.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmit2FA = async (): Promise<void> => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:5000/submit-2FA', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: twoFACode }),
        credentials: 'include',
      });
      const data = await response.json();
      if (response.ok) {
        showSuccessAndNavigate();
      } else {
        showError(data.message);
      }
    } catch (error) {
      showError('An error occurred while submitting 2FA code.');
    } finally {
      setIsLoading(false);
    }
  };

  const showSuccessAndNavigate = (): void => {
    toast({
      title: 'Scraping Complete',
      description: 'You are being redirected to the Solver Page.',
      status: 'success',
      duration: 2000, // Show the toast for 5 seconds
      isClosable: true,
    });
  
    // Navigate after the toast has been shown for its duration
    setTimeout(() => {
      router.push('/SolverPage');
    }, 2000); // Adjust the delay to match the toast's duration
  };

  const showError = (message: string): void => {
    toast({
      title: 'Error',
      description: message,
      status: 'error',
      duration: 5000,
      isClosable: true,
    });
  };

  return (
    <div className="flex h-screen bg-black">
      <div className="m-auto w-full max-w-6xl p-10 bg-gray-800 text-white shadow-xl rounded-xl">
        <h2 className="text-3xl font-bold mb-6">Gather Available Players</h2>
        <button
          onClick={handleScrapePlayers}
          disabled={isLoading}
          className="text-white bg-blue-500 hover:bg-blue-700 font-bold py-3 px-6 rounded-lg inline-flex items-center justify-center text-lg"
        >
          {isLoading ? <Spinner size="lg" color="white" /> : 'Start Gathering'}
        </button>
        {isLoading && (
          <div className="mt-4">
            <p className="text-lg">Scraping progress: {progress}%</p>
            <div className="bg-gray-700 h-2 rounded-full overflow-hidden">
              <div className="bg-blue-600 h-full" style={{ width: `${progress}%` }}></div>
            </div>
          </div>
        )}
        {is2FARequired && (
          <div className="mt-6 bg-gray-700 p-6 shadow-inner rounded-lg">
            <Input
              placeholder="Enter 2FA Code"
              value={twoFACode}
              onChange={(e) => setTwoFACode(e.target.value)}
              size="lg"
              className="appearance-none block w-full bg-gray-800 text-white border border-gray-600 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-700 focus:border-gray-500 mt-2 text-lg"
              type="text"
            />
            <ChakraButton
              onClick={handleSubmit2FA}
              isLoading={isLoading}
              loadingText="Scraping your UT Club...."
              colorScheme="blue"
              variant="solid"
              size="lg"
              className="mt-4 py-3 px-6 text-lg"
              sx={{
                background: 'bg-blue-500', 
                color: 'white',
                fontWeight: 'bold',
                borderRadius: 'md', 
                paddingY: '1.5rem', 
                paddingX: '1.5rem', 
                fontSize: 'lg', 
              }}
            >
              Submit 2FA Code
            </ChakraButton>
          </div>
        )}
        <p className="mt-4 text-lg">Relax, this may take a minute or two.</p>
        <p className="mt-4 text-lg">After Successful Scraping of your Ultimate Team Club
                                    we will redirect you to the next step!</p>
      </div>
    </div>
  );
}
export default ScrapeSolvePage;

