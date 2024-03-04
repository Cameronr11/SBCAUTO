"use client";
import React from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import { useRouter } from 'next/navigation';
import CustomButton from '@/components/CustomButton'

export const SignInPage = () => {

  const handleSignInClick = () => {
    router.push('/ScrapeSolvePage')
  }

  const router = useRouter();
  
  interface SignInFormData {
    username: string;
    password: string;
  }

  const { register, handleSubmit } = useForm<SignInFormData>();

  const onSubmit = async (data: SignInFormData) => {
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        credentials: 'include',
      });
      if (response.ok) {
        // Handle successful submission here
        const responseData = await response.json();
        console.log('Success:', responseData);
        router.push('/ScrapeSolvePage') //move to the end when api integrated
      } else {
        // Handle errors or unsuccessful submission here
        console.error('Failed to submit form');
      }
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  }
  return (
    <div className="min-h-screen flex items-center justify-center bg-black">
      <form onSubmit={handleSubmit(onSubmit)} className="w-full max-w-md bg-gray-900 p-8 rounded-lg shadow-md">
        <div className="mb-4">
          <p className='text-white text-sm font-bold mb-2'>
            Sign In using your EA FC 24 credentials
          </p>
          <label className="block text-white text-sm font-bold mb-2" htmlFor="username">
            Username
          </label>
          <input {...register("username")} className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username" />
        </div>
        <div className="mb-6">
          <label className="block text-white text-sm font-bold mb-2" htmlFor="password">
            Password
          </label>
          <input {...register("password")} className="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" />
        </div>
        <div className="flex items-center justify-between">
          <CustomButton
            title= 'Sign in'
            btnType='button'
            containerStyles='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline'
            handleClick={handleSignInClick}
            />
        </div>
      </form>
    </div>
  );
};

export default SignInPage
