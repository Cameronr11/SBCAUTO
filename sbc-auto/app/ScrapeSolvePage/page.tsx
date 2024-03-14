"use client";
import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Spinner, useToast, Input, Button as ChakraButton, Box, Text, Button } from '@chakra-ui/react';

const ScrapeSolvePage = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [is2FARequired, setIs2FARequired] = useState(false);
  const [twoFACode, setTwoFACode] = useState('');
  const router = useRouter();
  const toast = useToast();

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
      description: 'You can now proceed to the Solver Page.',
      status: 'success',
      duration: null, // Requires user action to close
      isClosable: true,
      render: () => (
        <Box p={3} bg="green.500" color="white" display="flex" flexDirection="column" alignItems="center">
          <Text>Scraping successful! Click below to proceed.</Text>
          <Button mt={2} colorScheme="teal" onClick={() => router.push('/SolverPage')}>
            Go to Solver Page
          </Button>
        </Box>
      ),
    });
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
        <h2 className="text-3xl font-bold mb-6">Step 1: Gather Available Players</h2>
        <button
          onClick={handleScrapePlayers}
          disabled={isLoading}
          className="text-white bg-blue-500 hover:bg-blue-700 font-bold py-3 px-6 rounded-lg inline-flex items-center justify-center text-lg"
        >
          {isLoading ? <Spinner size="lg" color="white" /> : 'Start Gathering'}
        </button>
        {is2FARequired && (
          <div className="mt-6 bg-gray-700 p-6 shadow-inner rounded-lg">
            <Input
              placeholder="Enter 2FA Code"
              value={twoFACode}
              onChange={(e) => setTwoFACode(e.target.value)}
              size="lg"
              className="mt-2 text-lg"
            />
            <ChakraButton
              onClick={handleSubmit2FA}
              isLoading={isLoading}
              loadingText="Submitting"
              colorScheme="blue"
              variant="solid"
              size="lg"
              className="mt-4 py-3 px-6 text-lg"
            >
              Submit 2FA Code
            </ChakraButton>
          </div>
        )}
        <p className="mt-4 text-lg">Relax, this may take a minute or two.</p>
      </div>
    </div>
  );
};

export default ScrapeSolvePage;


