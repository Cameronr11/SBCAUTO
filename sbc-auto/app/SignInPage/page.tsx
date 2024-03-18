"use client";
import React from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import { useRouter } from 'next/navigation';
import CustomButton from '@/components/CustomButton'
import { Eye, EyeOff } from 'lucide-react';

export const SignInPage = () => {

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
        localStorage.setItem('isSignedIn', 'true');
        router.push('/ScrapeSolvePage') //move to the end when api integrated
      } else {
        // Handle errors or unsuccessful submission here
        console.error('Failed to submit form');
      }
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  }

  const [showPassword, setShowPassword] = React.useState(false);

  const togglePasswordVisibility = () => setShowPassword(!showPassword);

  return (
    <div className="min-h-screen flex items-center justify-center bg-black">
      <form onSubmit={handleSubmit(onSubmit)} className="w-full max-w-md bg-gray-900 p-8 rounded-lg shadow-md space-y-4">
        <p className='text-white text-sm font-bold'>
          Sign In using your EA FC 24 credentials
        </p>
        <div className="mb-4">
          <label htmlFor="username" className="block text-white text-sm font-bold mb-2">
            Username
          </label>
          <input {...register("username")} id="username" type="text" placeholder="Username" className="shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div className="mb-6 relative">
          <label className="block text-white text-sm font-bold mb-2" htmlFor="password">
            Password
          </label>
          <input
            {...register("password")}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline pr-10"
            id="password"
            type={showPassword ? "text" : "password"}
            placeholder="******************"
          />
          <button
            type="button"
            onClick={() => setShowPassword(!showPassword)}
            className="absolute inset-y-0 right-0 pr-3 flex items-center justify-center"
          >
            {showPassword ? <EyeOff size={20} color="white" /> : <Eye size={20} color="white" />}
          </button>
        </div>

        <div className="flex items-center justify-between">
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Sign In
          </button>
        </div>
      </form>
    </div>
  );
};

export default SignInPage;